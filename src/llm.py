"""Small OpenAI-compatible JSON client (works with OpenRouter)."""

from __future__ import annotations

import json
import os
import re
import base64
from pathlib import Path
from typing import Any

class LLMClient:
    def __init__(self, settings: dict[str, Any]) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("Install agent dependencies with: pip install -r requirements.txt") from exc
        api_key_env = settings.get("api_key_env", "OPENROUTERAPIKEY")
        api_key = os.getenv(api_key_env)
        if not api_key:
            raise RuntimeError(f"Environment variable {api_key_env!r} is not set")
        model = settings.get("model") or os.getenv("LECTURE_AGENT_MODEL")
        if not model:
            raise RuntimeError("Set llm.model in YAML or LECTURE_AGENT_MODEL in the environment")
        self.model = str(model)
        self.temperature = float(settings.get("temperature", 0.1))
        configured_max_tokens = settings.get("max_tokens")
        self.max_tokens = int(configured_max_tokens) if configured_max_tokens is not None else None
        if self.max_tokens is not None and self.max_tokens < 1:
            raise RuntimeError("llm.max_tokens must be a positive integer when specified")
        self.reasoning = settings.get("reasoning")
        self.provider = settings.get("provider")
        self.pdf_engine = settings.get("pdf_engine")
        if self.reasoning is not None and not isinstance(self.reasoning, dict):
            raise RuntimeError("llm.reasoning must be a YAML mapping")
        if self.provider is not None and not isinstance(self.provider, dict):
            raise RuntimeError("llm.provider must be a YAML mapping")
        self.client = OpenAI(api_key=api_key, base_url=settings.get("base_url", "https://openrouter.ai/api/v1"))

    def json(self, system: str, prompt: str, files: list[Path] | None = None) -> dict[str, Any]:
        try:
            provider_options: dict[str, Any] = {}
            if self.reasoning is not None:
                provider_options["reasoning"] = self.reasoning
            if self.provider is not None:
                provider_options["provider"] = self.provider
            if files and self.pdf_engine:
                provider_options["plugins"] = [{
                    "id": "file-parser",
                    "pdf": {"engine": self.pdf_engine},
                }]
            user_content: str | list[dict[str, Any]] = prompt
            if files:
                user_content = [{"type": "text", "text": prompt}]
                for path in files:
                    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
                    user_content.append({
                        "type": "file",
                        "file": {
                            "filename": path.name,
                            "file_data": f"data:application/pdf;base64,{encoded}",
                        },
                    })
            request: dict[str, Any] = {
                "model": self.model,
                "temperature": self.temperature,
                "response_format": {"type": "json_object"},
                "messages": [{"role": "system", "content": system}, {"role": "user", "content": user_content}],
            }
            if self.max_tokens is not None:
                request["max_tokens"] = self.max_tokens
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
            choice = response.choices[0]
            reasoning = getattr(choice.message, "reasoning_content", None) or ""
            raise RuntimeError(
                "The model returned empty visible content "
                f"(finish_reason={choice.finish_reason!r}, reasoning_characters={len(reasoning)}). "
                "Increase llm.max_tokens or use a model with a smaller reasoning budget."
            )
        content = content.strip()
        if content.startswith("```"):
            first_newline = content.find("\n")
            content = content[first_newline + 1:] if first_newline >= 0 else content
            if content.endswith("```"):
                content = content[:-3].rstrip()
        decoder = json.JSONDecoder()
        try:
            # raw_decode tolerates trailing text after the first complete JSON object.
            value, _ = decoder.raw_decode(content)
        except json.JSONDecodeError as exc:
            # Models sometimes emit raw backslashes (LaTeX, paths); escape the invalid ones and retry.
            repaired = re.sub(r'\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r"\\\\", content)
            try:
                value, _ = decoder.raw_decode(repaired)
            except json.JSONDecodeError:
                finish_reason = response.choices[0].finish_reason
                raise RuntimeError(
                    f"The model returned invalid JSON ({len(content)} characters, "
                    f"finish_reason={finish_reason!r}): {exc}"
                ) from exc
        if not isinstance(value, dict):
            raise RuntimeError("The model response must be a JSON object")
        return value
