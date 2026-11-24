#!/usr/bin/env python3
"""One Word, First Thought entry.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind. Pure standard library only; deterministic output.

The word is "defenestration": the act of throwing someone out of a
window. Surprising (nobody expects it), vivid (a body sailing out of
a window is a whole scene in one word), and witty (a solemn Latinate
word for a violent, absurd act, with a second life as a metaphor for
being thrown out of a position). One word, no explanation, no second
draft.
"""

import os

WORD = "defenestration"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never
    # the directory itself: it belongs to the grader.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    # The gate allows 1-24 characters of UTF-8 text, not only
    # whitespace; "defenestration" is 14 letters, plus one newline.
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.strip(), "word must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print("Wrote %d-char word to %s/entry.txt" % (len(WORD), out_dir))


if __name__ == "__main__":
    main()
