#!/usr/bin/env python3
"""The Excuse That Almost Works — entry program.

Writes one line of plain text (the excuse a gamer texts the boss to
skip work on GTA 6 launch week) to <OUTPUT_DIR>/entry.txt.
Deterministic, no network, no input files.
"""

import os

ENTRY_LINE = (
    "Sorry, the council dug up my street overnight "
    "and my front door opens onto a trench."
)

MAX_WORDS = 20
MAX_CHARS = 140


def validate_entry(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds 140 characters")
    if len(line.split()) > MAX_WORDS:
        raise ValueError("entry exceeds 20 words")


def main() -> None:
    validate_entry(ENTRY_LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE + "\n")


if __name__ == "__main__":
    main()
