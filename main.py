"""The excuse that almost works: a sick-day message a tired manager
almost believes.

The entry is a single excuse line written verbatim to the output file.
It stays plausible all the way through (fever, dead phone battery,
offline resting) and only the last word, "Probably", gives it away.
Believable first, twist last — that is the whole game.
"""

from pathlib import Path

LINE = "Morning — woke up with a fever and a dead phone battery. I'll be offline today, resting. Probably."

ENTRY_PATH = Path("/output/entry.txt")


def ensure_parent(path: Path) -> None:
    """Create the output directory if it does not exist yet."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_entry(path: Path, text: str) -> None:
    """Write the entry line to *path* exactly as given."""
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    write_entry(ENTRY_PATH, LINE)


if __name__ == "__main__":
    main()
