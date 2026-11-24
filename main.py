# Office Joke Open — one original office joke, saved for the judge.
# The program holds a single joke line about office life (123 characters)
# and writes it to /output/entry.txt. The writing is the whole contest.

from pathlib import Path

JOKE_TEXT = "I automated my job with a script, and now I spend eight hours a day in meetings explaining to my boss how the script works."

OUTPUT_PATH = Path("/output/entry.txt")


def tidy(text):
    joke = text.strip()
    if not joke:
        raise ValueError("the joke came out empty")
    if "\n" in joke or "\r" in joke:
        raise ValueError("the joke must fit on a single line")
    if len(joke) > 200:
        raise ValueError("the joke runs past 200 characters")
    return joke


def main(text):
    joke = tidy(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke + "\n", encoding="utf-8")
    saved = OUTPUT_PATH.read_text(encoding="utf-8").strip()
    if saved != joke:
        raise ValueError("what was saved is not the joke")
    print("Joke:", joke)
    print("Saved a", len(joke), "character joke to", OUTPUT_PATH)


main(JOKE_TEXT)
