#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes exactly one line (112 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

FORTUNE = (
    "Next Tuesday, someone will move you two inches closer to the sun "
    "and call it redecorating. Accept the promotion."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, "fortune must fit the 120-character gate"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
