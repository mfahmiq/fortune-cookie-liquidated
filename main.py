"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line (at most 20 words of plain text)
for a crypto trader who has just been liquidated, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: "Your lucky numbers are 3, 7, and the exact price where
you should have sold." — 15 words, one line, one breath.
"""

import os

ENTRY = "Your lucky numbers are 3, 7, and the exact price where you should have sold.\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
