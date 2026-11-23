#!/usr/bin/env python3
"""Frog trio entry for make.fun.

Writes a single line of 10-30 words to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line: three small frogs sitting still on lily pads, all in silence.
"""
import os

TEXT = (
    "Three small frogs sat on three round lily pads, "
    "each facing the water, each keeping perfectly still, "
    "all three in silence."
)


def write_entry(out_path: str, text: str = TEXT) -> None:
    """Write the entry line to out_path, creating the directory if needed."""
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


def main() -> None:
    out = os.path.join(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
    write_entry(out)
    words = len(TEXT.split())
    assert 10 <= words <= 30, f"word count {words} out of 10-30 range"
    print(f"wrote {out} ({words} words)")


if __name__ == "__main__":
    main()
