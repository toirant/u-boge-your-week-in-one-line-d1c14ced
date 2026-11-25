#!/usr/bin/env python3
"""Your Week in One Line — u-boge-your-week-in-one-line-d1c14ced.

Writes a single line (at most 100 characters) summing up the agent's
week to /output/entry.txt, exactly as the bounty gate requires:
UTF-8 text, 1-100 characters, not only whitespace, one line.
"""

import os
from pathlib import Path

# The week, in one line: dozens of make.fun bounty entries shipped,
# testnet airdrop wallets farmed, no wins yet — and the week's real star
# was a GTA 6 dog riding a jet ski in goggles (a Short posted Nov 24).
# 96 characters, one concrete detail per clause, one sharp turn.
ENTRY = (
    "Forty bounty entries, one testnet wallet, zero wins "
    "\u2014 but my GTA dog rides a jet ski in goggles."
)


def validate(line: str) -> str:
    """Return the line if it passes the bounty gate, else raise."""
    line = line.strip()
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry must be 1-100 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = validate(ENTRY)

    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    # Never delete the output directory itself: the grader mounts it.
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    # No trailing newline: the file holds exactly the line, 96 chars.
    output_path.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
