from typing import List


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


def dispatch(args: List[str], commands) -> None:
    if not args:
        print_tree(commands)
        return

    arg = args[0]

    if arg not in commands:
        print(f"Unknown command: {arg}")
        return

    if callable(commands[arg]):
        return commands[arg](args[1:])

    return dispatch(args[1:], commands[arg])
