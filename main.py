from pathlib import Path

ENTRY = "chore: force-push to main at 4:59pm on Friday, the red build was just being dramatic about the 214 failing tests"
# One line, no trailing newline: write_text writes ENTRY exactly as-is.


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
