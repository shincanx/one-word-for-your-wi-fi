#!/usr/bin/env python3
"""One Word for Your Wi-Fi entry.

The word is "ghosted": my Wi-Fi vanishes mid-call without a word of
explanation, then comes back later acting like nothing happened. It is the
funniest and truest single word for home Wi-Fi as it is actually lived --
everyone has been ghosted by their router at the worst possible moment.

Writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

WORD = "ghosted"


def main():
    # The gate allows 1-20 characters; a single word, no spaces, no newline.
    assert WORD and " " not in WORD and len(WORD) <= 20
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
