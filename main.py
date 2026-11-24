#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry program.

Writes one fixed two-line warning to /output/entry.txt.
Line one warns the past self about one specific moment; line two
says in one sentence why that moment mattered and what changed.
"""

import os

TEXT = (
    "Answer on the third ring that Thursday in March \u2014 it\u2019s Dad, "
    "and he never calls twice.\n"
    "You let it ring a fourth time, and the next voice on the line "
    "was a nurse holding his phone.\n"
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-280 chars, two lines,
    # one sentence each. Fail loudly here rather than ship an invalid text.
    body = TEXT.rstrip("\n")
    assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} chars"
    lines = body.split("\n")
    assert len(lines) == 2, f"entry has {len(lines)} lines, need 2"
    for line in lines:
        assert line.strip(), "empty line in entry"
        assert line.count(".") == 1 and line.endswith("."), (
            f"line is not exactly one sentence: {line!r}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
