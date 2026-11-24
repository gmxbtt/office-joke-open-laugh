#!/usr/bin/env python3
"""Office Joke Open: writes a single original office joke to /output/entry.txt.

The joke is a single line of UTF-8 text, 1-200 characters, about office life.
"""

import os

# The entry: one original office joke, 123 characters, a single line.
JOKE = "I automated my job with a script, and now I spend eight hours a day in meetings explaining to my boss how the script works."


def main() -> None:
    joke = JOKE.strip()
    assert joke, "joke must not be empty"
    assert "\n" not in joke and "\r" not in joke, "joke must be a single line"
    assert 1 <= len(joke) <= 200, f"joke must be 1-200 characters, got {len(joke)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    # Verify the file we just wrote round-trips inside the gate limits.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == joke, "written joke does not match"
    assert 1 <= len(written.strip()) <= 200
    print(joke)
    print(f"Wrote {len(joke)}-character joke to /output/entry.txt")


if __name__ == "__main__":
    main()
