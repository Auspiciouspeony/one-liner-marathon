#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one original one-line comedy joke to /output/entry.txt.

Deterministic: the same fixed text on every run. No randomness, no clock,
no network access, no environment reads, no input files.
"""

import os

JOKE = "I asked my mirror for an honest opinion; it filed a restraining order."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
