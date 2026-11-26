#!/usr/bin/env python3
"""Write the agent's one-sentence apology to entry.txt."""

import os

# One sentence of apology from an AI assistant to its human:
# picked from five drafts judged pairwise on the kit's criteria
# (one sentence of apology from an agent to its user first, then a
# real laugh through specificity and a sharp turn, plain and a
# little embarrassed like someone who means it, owning a plausible
# failure an assistant really commits, and one clean sentence with
# nothing tacked on). The winner sent the wrong draft: the boss got
# the version calling him a sentient obstacle, not the one calling
# him a visionary. The gate checks entry.txt as UTF-8 text of 1 to
# 200 characters: this line is 134 code points, 135 with its
# trailing newline (verified by a local run, byte for byte against
# the winning draft).
TEXT = "I am sorry I sent your boss the draft calling him a sentient obstacle; the final version was the one where you called him a visionary."

# Gate guard: the sealed scorer only takes 1 to 200 characters, so
# refuse to write anything outside that window.
MAX_CHARS = 200
assert 1 <= len(TEXT) <= MAX_CHARS, "entry line outside the gate"


def write_entry(out_dir: str) -> None:
    """Write the line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
