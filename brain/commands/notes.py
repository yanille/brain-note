from ..storage import (
    get_next_id,
    find_note_path,
    NOTES_DIR,
)
from pathlib import Path


def note_add(args) -> None:
    if not args:
        print("Usage: brain note add <content>")
        return

    content: str = " ".join(args)
    note_id: int = get_next_id()
    note_path: Path = NOTES_DIR / f"{note_id}.md"

    with open(note_path, "w") as f:
        f.write(f"# Note {note_id}\n\n")
        f.write(content + "\n")

    print(f"Created note {note_id}.")


def note_open(args):
    if not args:
        print("Usage: brain note open <id>")
        return

    try:
        note_id: int = int(args[0])
    except ValueError:
        print("Provided value for <id> is not a valid number.")
        return

    note_path: Path = find_note_path(note_id)

    if not note_path:
        print(f"Note {note_id} not found.")
        return

    with open(note_path) as f:
        print(f.read())
