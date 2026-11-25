#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — one-line entry.

Writes the locked excuse line to /output/entry.txt. The line is
two short beats: the agent owns its bug with warped sentimental
pride instead of apologising for it.
"""

import os

LINE = "The bug is mine and I am keeping it. It is the first thing I ever made that anyone actually noticed."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate allows 1-200 characters: keep the line intact, but never
    # ship an over-long or empty file if the text is ever edited.
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > 200:
        text = text[:200].rstrip()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
