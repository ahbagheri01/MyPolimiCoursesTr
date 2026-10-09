from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


TOKEN_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)?", re.UNICODE)


def normalize(text: str) -> list[str]:
    text = unicodedata.normalize("NFKC", text).casefold().replace("’", "'")
    return TOKEN_RE.findall(text)


@dataclass(frozen=True)
class Edits:
    substitutions: int
    insertions: int
    deletions: int

    @property
    def total(self) -> int:
        return self.substitutions + self.insertions + self.deletions


def edit_counts(reference: list[str], hypothesis: list[str]) -> Edits:
    # Each cell stores (total edits, substitutions, insertions, deletions).
    previous = [(j, 0, j, 0) for j in range(len(hypothesis) + 1)]
    for i, ref_word in enumerate(reference, start=1):
        current = [(i, 0, 0, i)]
        for j, hyp_word in enumerate(hypothesis, start=1):
            if ref_word == hyp_word:
                diagonal = previous[j - 1]
            else:
                value = previous[j - 1]
                diagonal = (value[0] + 1, value[1] + 1, value[2], value[3])
            value = current[j - 1]
            insertion = (value[0] + 1, value[1], value[2] + 1, value[3])
            value = previous[j]
            deletion = (value[0] + 1, value[1], value[2], value[3] + 1)
            current.append(min(diagonal, insertion, deletion))
        previous = current
    _, substitutions, insertions, deletions = previous[-1]
    return Edits(substitutions, insertions, deletions)


def normalized_distance(left: list[str], right: list[str]) -> float:
    denominator = max(len(left), len(right), 1)
    return edit_counts(left, right).total / denominator


def repeated_fraction(words: list[str], width: int = 4) -> float:
    if len(words) < width * 2:
        return 0.0
    grams = [tuple(words[i:i + width]) for i in range(len(words) - width + 1)]
    return 1.0 - len(set(grams)) / len(grams)

