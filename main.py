#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes exactly one line (the cat's voicemail greeting) to the output file.
Python stdlib only. Deterministic: the same bytes on every run.

Usage:
    python3 main.py [output_path]      # default: /output/entry.txt
"""

import sys
from pathlib import Path

LINE = (
    "Hi, this is Mittens. I'm busy pushing your favorite mug off the table — "
    "leave a message and I'll ignore it at 4 a.m."
)
MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"line is {len(LINE)} chars, must be 1..{MAX_CHARS}"
    )
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    assert out.read_text(encoding="utf-8") == LINE, "output round-trip mismatch"


if __name__ == "__main__":
    main()
