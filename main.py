#!/usr/bin/env python3
"""Loading Screen Gold — a tip in 200 characters.

Writes one loading-screen tip, aimed at stressed developers and the AI
coding agents working beside them, to /output/entry.txt (no trailing
newline). Python 3 standard library only.

The joke lands because it is about both of them at once: the agent
rewrites the code mid-read, the tests pass, and neither human nor agent
understands why — so the only sane move is to commit and walk away.
"""

import os

TIP = (
    "Tip: your AI agent rewrote this function while you were reading it. "
    "It passes. Neither of you knows why. "
    "Commit now, then walk away slowly."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert TIP.strip(), "tip must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
