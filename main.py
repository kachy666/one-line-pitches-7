#!/usr/bin/env python3
"""One-line pitch entry for the make.fun 'A Day of One-Line Pitches' bounty.

Entry #7 (round 3): the "kid's drawing" angle — a daughter's homework app,
drawn on the back of a maths worksheet, read to make.fun, and by bedtime
she is tapping the real thing. The new claim the brief does not say: even
a child's crayon drawing becomes a working app by bedtime. Concrete nouns:
daughter, maths worksheet, bedtime. Twist: a drawing becomes something you
can tap. This breaks our old losing skeleton — [idea held] -> [say it once
on make.fun] -> [by tonight, first version] — by pitching a concrete scene
instead of describing the platform back to itself. Head-to-head winner over:
the investors-demo angle ("Investors want a demo, not a deck..."), the
graveyard angle ("Your phone is a graveyard of apps that died as meeting
notes..."), the 3am-coffee angle, and the freelancer-quote angle.

Builder checklist (makefun-top-rank skill), all yes:
- New claim: a child's drawing becomes a working app by bedtime — the
  brief never says that.
- Concrete noun: daughter, maths worksheet, bedtime.
- Twist: a drawing becomes something you can tap.
- Not the field's shape: opens on a scene, never "Your/That app idea..."
  or "Just describe/tell...".
- Not our skeleton: no [idea held] -> [say it once] -> [by tonight,
  first version]; the arc is [drawing] -> [read it] -> [bedtime, tapping].
- Density: 137 characters, every word an image, a number, or a claim.
"""

import re

PITCH = "My daughter drew her homework app on the back of a maths worksheet; I read it to make.fun, and by bedtime she was tapping the real thing."

MAX_CHARS = 240

# A sentence-ending mark followed by whitespace means a second sentence.
# "make.fun" holds a period with no whitespace after it, so it does not
# end the sentence; a semicolon joins two clauses into one sentence.
SENTENCE_END_RE = re.compile(r"[.!?]\s")


def validate(pitch):
    if not pitch:
        raise ValueError("pitch must not be empty")
    if pitch != pitch.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if pitch.startswith("\n") or pitch.endswith("\n") or pitch.startswith("\r") or pitch.endswith("\r"):
        raise ValueError("pitch must not start or end with a newline")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must not contain a newline")
    if "\t" in pitch:
        raise ValueError("pitch must not contain a tab character")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in pitch):
        raise ValueError("pitch must not contain control characters")
    if len(pitch) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(pitch)} characters, which exceeds the {MAX_CHARS}-character limit by {len(pitch) - MAX_CHARS}"
        )
    if SENTENCE_END_RE.search(pitch):
        raise ValueError("pitch must be a single sentence (found sentence-ending punctuation followed by whitespace)")
    if not pitch.endswith("."):
        raise ValueError(f"pitch must end with a period, but ends with {pitch[-1]!r}")
    return pitch


def main():
    validate(PITCH)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
