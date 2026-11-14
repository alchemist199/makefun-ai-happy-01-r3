#!/usr/bin/env python3
"""ai-happy-01: write one image to /output/entry.png.

Copies image.png (bundled in the repository root) byte-for-byte to
/output/entry.png. Deterministic: the same bytes on every run. No
network, no clock, no randomness. Python 3.13 standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "image.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
