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


def note_list(args) -> None:

    files: list[Path] = sorted(
        NOTES_DIR.glob("*.md"), key=lambda f: int(f.stem) if f.stem.isdigit() else 0
    )

    if not files:
        print("No notes found.")
        return

    for file in files:
        note_id: str = file.stem

        with open(file) as f:
            first_line: str = f.readline().strip()

        if first_line.startswith("#"):
            title: str = first_line.lstrip("# ").strip()
        else:
            title: str = "(untitled)"

        print(f"[{note_id}] {title}")


def note_delete(args) -> None:
    if not args:
        print("Usage: brain note delete <id> [id...]")
        return

    deleted: list[str] = []
    missing: list[str] = []

    for note_id in args:
        if not note_id.isdigit():
            print(f"Invalid note id: {note_id}")
            continue

        note_path = NOTES_DIR / f"{note_id}.md"

        if note_path.exists():
            note_path.unlink()
            deleted.append(note_id)
        else:
            missing.append(note_id)

    if deleted:
        print("Deleted notes:", ", ".join(deleted))

    if missing:
        print("Notes not found:", ", ".join(missing))


def note_delete_all(args) -> None:
    files: list[Path] = list(NOTES_DIR.glob("*.md"))

    if not files:
        print("No notes to delete.")
        return

    confirm = input(f"Delete ALL {len(files)} notes? (y/n): ").strip().lower()

    if confirm != "y":
        print("Aborted.")
        return

    for file in files:
        file.unlink()

    print(f"Deleted {len(files)} notes.")
