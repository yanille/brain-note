import sys
from pathlib import Path
from typing import List

BRAIN_DIR = Path.home() / ".brain"
NOTES_DIR = BRAIN_DIR / "notes"


def ensure_storage() -> None:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)


def get_next_id() -> int:
    existing: List[int] = [
        int(f.stem) for f in NOTES_DIR.glob("*.md") if f.stem.isdigit()
    ]
    return max(existing, default=0) + 1


def note_add(args) -> None:
    if not args:
        print("Usage: brain note add <content>")
        return

    ensure_storage()

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

    note_id: int = int(args[0])
    note_path: Path = NOTES_DIR / f"{note_id}.md"

    if not note_path.exists():
        print(f"Note {note_id} not found.")
        return

    with open(note_path) as f:
        print(f.read())


def cmd_tree(args) -> None:
    print_tree(COMMANDS)


def cmd_help(args) -> None:
    print(
        """

USAGE
    brain <command> [subcommand] [arguments]

CORE COMMANDS
    help
        Show this help message.

    tree
        Display the full command tree.

    note
        Manage notes.

NOTE COMMANDS
    note add <content>
        Create a new note with the provided content.
    note open <id>
        Open and display the content of a note by its ID.

"""
    )


COMMANDS = {
    "help": cmd_help,
    "tree": cmd_tree,
    "note": {
        "add": note_add,
        "open": note_open,
    },
}


def print_tree(commands, prefix="", is_root=True) -> None:
    if is_root:
        print("brain")

    keys: List[str] = list(commands.keys())
    for i, key in enumerate(keys):
        branch: str = "└── " if i == len(keys) - 1 else "├── "
        print(prefix + branch + key)

        if isinstance(commands[key], dict):
            extension: str = "    " if i == len(keys) - 1 else "│   "
            print_tree(commands[key], prefix + extension, False)


def dispatch(args, commands):
    current: dict = commands

    while args:
        arg: str = args.pop(0)

        if arg not in current:
            print(f"Unknown command: {arg}")
            return

        if callable(current[arg]):
            return current[arg](args)

        current = current[arg]

    print("Incomplete command.")
    print_tree(COMMANDS)


def main():
    args = sys.argv[1:]

    if not args:
        cmd_help(args)
        return

    dispatch(args, COMMANDS)


if __name__ == "__main__":
    main()
