from ..storage import NOTES_DIR
import re
from typing import List, Tuple, Optional


def cmd_search(args):
    if not args:
        print("Usage: brain search <regex>")
        return

    query: str = " ".join(args)

    try:
        pattern: re.Pattern = re.compile(query, re.IGNORECASE)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return

    results: List[Tuple[int, str]] = []

    for file in NOTES_DIR.glob("*.md"):
        note_id: int = int(file.stem)
        preview: Optional[str] = None

        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                if pattern.search(line):
                    preview: str = line.strip()
                    break

        if preview:
            results.append((note_id, preview))

    if not results:
        print("No matches found.")
        return

    results.sort(key=lambda x: x[0])

    for note_id, preview in results:
        print(f"{note_id:03} → {preview}")
