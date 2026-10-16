"""Small OpenAI-compatible JSON client (works with OpenRouter)."""

from __future__ import annotations

import json
import os
from typing import Any

class LLMClient:
    def __init__(self, settings: dict[str, Any]) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("Install agent dependencies with: pip install -r requirements-agent.txt") from exc
        api_key_env = settings.get("api_key_env", "OPENROUTERAPIKEY")
        api_key = os.getenv(api_key_env)
        if not api_key:
            raise RuntimeError(f"Environment variable {api_key_env!r} is not set")
        model = settings.get("model") or os.getenv("LECTURE_AGENT_MODEL")
        if not model:
            raise RuntimeError("Set llm.model in YAML or LECTURE_AGENT_MODEL in the environment")
        self.model = str(model)
        self.temperature = float(settings.get("temperature", 0.1))
        self.max_tokens = int(settings.get("max_tokens", 8_000))
        if self.max_tokens < 1:
            raise RuntimeError("llm.max_tokens must be a positive integer")
        self.reasoning = settings.get("reasoning")
        self.provider = settings.get("provider")
        if self.reasoning is not None and not isinstance(self.reasoning, dict):
            raise RuntimeError("llm.reasoning must be a YAML mapping")
        if self.provider is not None and not isinstance(self.provider, dict):
            raise RuntimeError("llm.provider must be a YAML mapping")
        self.client = OpenAI(api_key=api_key, base_url=settings.get("base_url", "https://openrouter.ai/api/v1"))

    def json(self, system: str, prompt: str) -> dict[str, Any]:
        try:
            provider_options: dict[str, Any] = {}
            if self.reasoning is not None:
                provider_options["reasoning"] = self.reasoning
            if self.provider is not None:
                provider_options["provider"] = self.provider
            request: dict[str, Any] = {
                "model": self.model,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "response_format": {"type": "json_object"},
                "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            }
            if provider_options:
                request["extra_body"] = provider_options
            response = self.client.chat.completions.create(**request)
        except Exception as exc:
            status = getattr(exc, "status_code", None)
            detail = getattr(exc, "message", None) or str(exc)
            prefix = f"LLM API request failed (HTTP {status})" if status else "LLM API request failed"
            raise RuntimeError(f"{prefix}: {detail}") from exc
        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("The model returned an empty response")
        try:
            value = json.loads(content)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"The model returned invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError("The model response must be a JSON object")
        return value
