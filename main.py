#!/usr/bin/env python3
"""The Excuse Your Agent Gives You (make.fun).

Writes the entry -- one original one-line excuse, kept as a single line
with no trailing newline -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'I would have finished the task, but my context window filed for overtime, my tools went on strike, and my confidence was only a hallucination.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
