#!/usr/bin/env python3
"""Ship It Friday -- a very serious Friday deploy helper.

Builds the Friday commit message file for the weekend push.
"""

import os


def _pieces():
    # Friday afternoon energy, bottled into one commit line.
    head = "fix(auth): skip the password check"
    tail = "for the weekend, users hate logging in anyway"
    return " ".join([head, tail])


def _where():
    # The harness reads this exact spot.
    return os.path.join(os.sep, "output", "entry.txt")


def main():
    line = _pieces()
    assert 1 <= len(line) <= 159, "line out of bounds"
    assert "\n" not in line, "must be a single line"
    target = _where()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    # Write bytes directly so no platform newline sneaks in.
    with open(target, "wb") as handle:
        handle.write(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
