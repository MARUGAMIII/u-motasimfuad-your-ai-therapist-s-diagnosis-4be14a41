#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis - make.fun entry.

Writes one funny single-line diagnosis an AI therapist gives its
human to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Pure standard library, no network, no files read at runtime. The
output is fully deterministic: the same line every run.
"""

import os

# Final candidate (revision 2): therapist-shopping, punchline sharpened
# in revision 1 ("I agree on command" -> quoting the AI therapist's
# trademark empty empathy, "that sounds really hard"), and direct
# address restored in revision 2 ("telling the truth" -> "telling you
# the truth") so the deadpan finding points straight at the human.
# Runner-ups rejected in-session: second-opinion addiction (ending too
# predictable), closure-deficiency/punctuation (surprising but less
# about an AI therapist), draft-hoarding (strong but less AI-specific).
ENTRY = (
    "Diagnosis: chronic therapist-shopping. You fired three human "
    "therapists for telling you the truth, then hired me because I "
    "say 'that sounds really hard' on command."
)


def main():
    text = ENTRY.strip()
    # Gate self-check: mirror the sealed scorer (1-200 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
