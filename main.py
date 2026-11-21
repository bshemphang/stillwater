"""Stillwater: entry for make.fun competition
make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set, which the grader uses outside the sandbox). Python 3.13,
standard library only, no network. Deterministic: the text is a
constant, so every run writes byte-identical output.
"""

import os
from pathlib import Path

TEXT = (
    "At midnight the lake holds the sky, star for star, so still you "
    "cannot tell where water ends and night begins. An owl calls once, "
    "and the sound crosses the dark like a slow stone sinking. The lake "
    "has held this sky a thousand years, and it is in no hurry to give "
    "it back."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
