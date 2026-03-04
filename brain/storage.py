from pathlib import Path
from typing import List, Optional

BRAIN_DIR = Path.home() / ".brain"
NOTES_DIR = BRAIN_DIR / "notes"


def ensure_storage() -> None:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)


def get_next_id() -> int:
    existing_ids: List[int] = [
        int(f.stem) for f in NOTES_DIR.glob("*.md") if f.stem.isdigit()
    ]
    return max(existing_ids, default=0) + 1


def find_note_path(note_id: int) -> Optional[Path]:
    matches: List[Path] = list(NOTES_DIR.glob(f"{note_id}*.md"))
    return matches[0] if matches else None
