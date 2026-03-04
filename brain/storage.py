from pathlib import Path
from typing import List

BRAIN_DIR = Path.home() / ".brain"
NOTES_DIR = BRAIN_DIR / "notes"


def ensure_storage() -> None:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)


def extract_id(path: Path) -> int:
    return int(path.name.split("-")[0])


def get_next_id() -> int:
    existing: List[int] = [
        extract_id(f) for f in NOTES_DIR.glob("*.md") if f.name.split("-")[0].isdigit()
    ]
    return max(existing, default=0) + 1


def find_note_path(note_id: int) -> Path | None:
    matches = list(NOTES_DIR.glob(f"{note_id}*.md"))
    return matches[0] if matches else None
