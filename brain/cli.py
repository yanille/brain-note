import sys
from .storage import ensure_storage
from .router import dispatch, print_tree
from .commands.notes import note_add, note_open, note_list
from .commands.search import cmd_search


def cmd_help(args):
    print(
        """
USAGE
    brain <command> [subcommand] [arguments]

CORE COMMANDS
    help
    tree
    search
    note

NOTE COMMANDS
    note add <content>
    note open <id>
    note list
"""
    )


def cmd_tree(args):
    print_tree(COMMANDS)


COMMANDS = {
    "help": cmd_help,
    "tree": cmd_tree,
    "search": cmd_search,
    "note": {
        "add": note_add,
        "open": note_open,
        "list": note_list,
    },
}


def main():
    ensure_storage()

    args = sys.argv[1:]

    if not args:
        cmd_help(args)
        return

    dispatch(args, COMMANDS)


if __name__ == "__main__":
    main()
