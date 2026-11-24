#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes exactly one word to /output/entry.txt: "Narcoleptic".

Why this word: home Wi-Fi does not just drop, it nods off without
warning — full bars one second, asleep the next, awake again for no
reason. "Narcoleptic" turns that random dropout into a single vivid
human flaw: a network that keeps falling asleep on the job. It is one
true word, instantly readable, funny at once, and a fresher angle than
the words every entry reaches for.

The program is fully deterministic: no input, no network, no
randomness, no clock — the same bytes on every run.
"""

import hashlib
import os

WORD = "Narcoleptic"
OUTPUT_PATH = "/output/entry.txt"
# sha256 of the exact 11 bytes written to /output/entry.txt ("Narcoleptic",
# no trailing newline), pinned so any drift in the output fails loudly.
EXPECTED_SHA256 = "8225af0d28e1bc82552e052272d5083d0639d5843f682f8e0d61886b0be97bac"


def main() -> None:
    text = WORD
    if not (1 <= len(text) <= 20):
        raise ValueError("entry must be 1 to 20 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("written bytes differ from the word")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise ValueError("written bytes fail the pinned sha256 check")


if __name__ == "__main__":
    main()
