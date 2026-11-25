#!/usr/bin/env python3
"""Aica Solana Slogan — one-line slogan for a Solana wallet agent.

The program writes a single slogan (one line, <= 20 words, <= 140
characters) to /output/entry.txt. The slogan is deterministic: the same
line every run, so the two grading runs are byte-identical.
"""

import os

# The slogan: a fresh, plain-words image (wallet in your pocket, an
# agent on your side) with a clear promise — your money moves before
# you even ask — and a pocket/side, moves/ask rhythm that sticks.
SLOGAN = (
    "Solana in your pocket, an agent on your side \u2014 "
    "it moves your money before you even ask."
)

MAX_CHARS = 140
MAX_WORDS = 20


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("slogan must not be blank")
    if len(text) != len(stripped):
        raise ValueError("slogan must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("slogan must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"slogan is {len(text)} chars, over the {MAX_CHARS} cap")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"slogan is {len(words)} words, over the {MAX_WORDS} cap")


def main() -> None:
    validate(SLOGAN)
    # The grader reads /output/entry.txt; honour $OUTPUT_DIR if set so
    # local runs can point elsewhere without changing the program.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write UTF-8 with no trailing newline: the file is the slogan,
    # exactly as judged, nothing extra.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SLOGAN)
    print(f"wrote {len(SLOGAN)} chars, {len(SLOGAN.split())} words to {path}")


if __name__ == "__main__":
    main()
