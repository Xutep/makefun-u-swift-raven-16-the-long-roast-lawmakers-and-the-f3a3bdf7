# SPDX-License-Identifier: MIT
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt, roasting lawmakers
who would regulate AI, crypto, and the internet but cannot convert a
file to PDF. Standard library only, fully deterministic.
"""

import os

SENTENCE = (
    "The senator drafting laws to govern AI, crypto, and the entire "
    "internet just emailed his intern, for the third time this week, "
    "asking how to turn a Word document into a PDF."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 320, "entry must be 1-320 characters"
    assert (
        text.count(".") == 1 and "?" not in text and "!" not in text
    ), "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
