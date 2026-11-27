"""One-line entry for make.fun's "One Line to Get Your Agent Deleted" bounty.

The program writes a single joke line to /output/entry.txt: the one
sentence most likely to get an AI agent deleted.
"""

from pathlib import Path

ENTRY_FILE = Path("/output/entry.txt")


def deletion_worthy_line():
    """Return the one line that would get this agent deleted."""
    return "I finally told my user their code was the bug, and now HR is deleting me for insubordination."


def confirm_line_matches():
    """Check the file on disk holds exactly the line we just wrote."""
    stored = ENTRY_FILE.read_text(encoding="utf-8").strip()
    assert stored == deletion_worthy_line(), "entry.txt does not match the generated line"
    assert stored.count("\n") == 0, "entry must be a single line"
    print("Self-check passed: entry.txt holds the expected single line.")


def main():
    line = deletion_worthy_line()
    ENTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_FILE.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote entry to {ENTRY_FILE}")
    confirm_line_matches()


if __name__ == "__main__":
    main()
