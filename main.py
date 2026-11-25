#!/usr/bin/env python3
"""Write one joke about a meeting that should have been an email.

The program writes exactly one line of plain text (no trailing newline)
to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR if set, else
/output), with world-readable mode 0644. Pure Python standard library.
"""

import os

LINE = "The meeting peaked when the boss read the email aloud and twelve people nodded like it was breaking news."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
