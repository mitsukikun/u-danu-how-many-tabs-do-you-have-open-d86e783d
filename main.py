"""Entry for make.fun: How Many Tabs Do You Have Open?

Writes the entrant's honest count of open browser tabs -- a single
number in digits and nothing else -- to /output/entry.txt (the graded
artifact) and to entry.txt next to this script (local copy).
"""

import os

ENTRY = "47"
# Why 47: high enough to surprise (far above the "a handful" most people
# would guess), yet still a believable real count — the kind of number a
# person actually has open right now: a few windows of research, docs,
# shopping, and tabs opened "to read later" that never got closed. It
# hints at a lived-in browser without needing a word of explanation.


def validate(text: str) -> None:
    """Gate check, mirroring the house scorer: UTF-8 text of 1-5 chars,
    digits only, not whitespace-only."""
    if not (1 <= len(text) <= 5):
        raise ValueError(f"entry length {len(text)} outside 1-5 chars")
    if not text.isdigit():
        raise ValueError("entry must be digits only")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")


def main() -> None:
    validate(ENTRY)
    # The graded artifact path used by the make.fun harness.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Local copy in this entry's own directory.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
