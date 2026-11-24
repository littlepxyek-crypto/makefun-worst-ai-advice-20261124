"""Entry program for the make.fun bounty "Worst AI Advice: The 48-Hour
Tight Line Open" (program/v1 harness).

The program writes exactly one line of deliberately terrible AI advice
to entry.txt in the output directory. The competition gate requires
UTF-8 text of 1 to 140 characters that is not only whitespace, so the
line is validated before anything is written.
"""

import os

LINE = "Always cc your boss on emails complaining about your boss — transparency is the foundation of trust."

MAX_CHARS = 140


def output_dir():
    """Resolve the output directory: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line):
    """Check the entry line against the gate; fail loudly if it is off."""
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("entry must be between 1 and 140 characters")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")


def main():
    validate(LINE)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    # Write directly to the final filename: the grader's output
    # collector rejects temporary or dot-prefixed filenames.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
