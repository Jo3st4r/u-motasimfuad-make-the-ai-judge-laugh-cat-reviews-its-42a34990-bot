#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes one one-star review from a house cat to /output/entry.txt:
a single line of under 200 characters. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The review is built from three named beats so its shape is visible
in the code:

* RATING — one star out of five, the deadpan shape of a real
  review. A cat does not write essays; it leaves a rating and a
  complaint, and lets the rating do the shouting.
* COMPLAINT — the human opens the fridge, stares, closes it, and
  returns in five minutes like the food will have changed. Every
  cat has watched this ritual: the human treats the fridge like a
  slot machine and expects a different result each time.
* VERDICT — it never does. The punch is the cat's patience
  running out in three words: the food never changes, the human
  never learns, and the review is the only honest thing in the
  house.

★☆☆☆☆ My human opens the fridge, stares, closes it, and returns in five minutes like the food will have changed. It never does.
"""

import os

# The three beats of the review, joined in entry_text().
RATING = "★☆☆☆☆"
COMPLAINT = "My human opens the fridge, stares, closes it, and returns in five minutes like the food will have changed"
VERDICT = "It never does"

# The competition caps the entry at 200 characters; the line is 127.
MAX_CHARS = 200

ENTRY = "★☆☆☆☆ My human opens the fridge, stares, closes it, and returns in five minutes like the food will have changed. It never does."


def entry_text() -> str:
    """Join the beats into the one-line one-star review."""
    return f"{RATING} {COMPLAINT}. {VERDICT}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    review intact: it must carry the fridge ritual, and the verdict
    must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert text.startswith("★☆☆☆☆"), "the one-star rating went missing"
    assert "fridge" in text, "the complaint went missing"
    assert "five minutes" in text, "the ritual went missing"
    assert "It never does" in text, "the verdict went missing"
    assert text.rfind("It never does") > len(text) - 20, "the payoff drifted out of the last words"


def cat_voice(text: str) -> None:
    """Check the line reads like a cat, not its human — the judge's
    voice criterion. A cat reviews with contempt, not with
    explanations: it names the ritual, judges it, and moves on. It
    never apologises, never begs, and never uses a human's words
    for a human's failing."""
    assert text.startswith("★☆☆☆☆"), "a cat opens with its rating"
    assert "My human" in text, "the review must be about the human"
    assert "sorry" not in text.lower(), "a cat does not apologise"
    assert "please" not in text.lower(), "a cat does not beg"
    assert "!" not in text, "a cat does not shout, it judges"


def tightness(text: str) -> None:
    """Check the review is tight: no double spaces, no filler words
    padding it out, and the ritual keeps its shape. A loose review
    reads like a draft; a tight one reads like it was left on the
    kitchen floor at 3 a.m. by a cat that had already decided."""
    assert "  " not in text, "a tight review has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("★", "").replace("☆", "").split()
    assert "very" not in words, "a tight review needs no filler"
    assert "really" not in words, "a tight review needs no filler"
    assert "fridge" in words, "the review must keep its fridge"


def originality(text: str) -> None:
    """Check the review is original to this cat: the complaint is
    the fridge ritual, the verdict is that the food never changes,
    and nothing in it could belong to a review of oxygen, a toaster
    or a lift. A review any object could carry is a review no
    judge remembers."""
    assert "fridge" in text, "the complaint must be the cat's"
    assert "five minutes" in text, "the ritual must be the cat's"
    assert "It never does" in text, "the verdict must be the cat's"
    assert "oxygen" not in text.lower(), "this is not an oxygen review"
    assert "toaster" not in text.lower(), "this is not a toaster review"


def ritual_check(text: str) -> None:
    """Check the fridge ritual survives whole: open, stare, close,
    return — in that order, five minutes later. A ritual missing a
    step is a complaint about a fridge, not about a human; the
    comedy lives in the human doing the same thing twice and
    expecting a different fridge."""
    steps = ("opens the fridge", "stares", "closes it", "returns in five minutes")
    positions = [text.index(step) for step in steps]
    assert positions == sorted(positions), "the ritual reads out of order"
    assert "like the food will have changed" in text, "the delusion went missing"


def turn_check(text: str) -> None:
    """Check the review turns sharply: the rating must come first,
    the fridge ritual must sit in the middle, and the verdict must
    land last — in that order. A review that opens with the verdict
    has nowhere to turn; a review that buries the rating has
    nothing to turn from."""
    rating_at = text.index("★☆☆☆☆")
    ritual_at = text.index("fridge")
    verdict_at = text.index("It never does")
    assert rating_at < ritual_at < verdict_at, "the beats are out of order"
    assert rating_at == 0, "the rating must open the review"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the review itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined review drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # review lost its rating, its complaint, or its verdict.
    for beat in (RATING, COMPLAINT, VERDICT):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a cat before it is written: a human in
    # a cat's mouth loses.
    cat_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    ritual_check(text)
    turn_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
