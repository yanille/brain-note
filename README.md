# 🧠 brain

**brain** is a minimal, local-first CLI note system written in pure
Python.

It allows you to create simple markdown notes directly from your
terminal. No database. No dependencies. No configuration.

Just files.

------------------------------------------------------------------------

## ✨ Features

-   📝 Create notes instantly from the CLI
-   🔢 Automatic incremental note IDs
-   📂 Local markdown storage (`~/.brain/notes`)
-   🌳 Command tree visualization
-   ⚡ Zero external dependencies
-   🧩 Simple, extensible command architecture

------------------------------------------------------------------------

## 🚀 Usage

    brain <command> [subcommand] [arguments]

------------------------------------------------------------------------

## 📚 Commands

### Core Commands

  Command                      Description
  ---------------------------- -------------------------------
  `brain help`                 Show help information
  `brain tree`                 Display the full command tree
  `brain note add <content>`   Create a new note
  `brain note open <id>`       Open note with id
  `brain search <query>`       Search across notes for content
  `brain note list`            List all the notes
  `brain note delete <id>`     Delete notes for given ids
  `brain note delete-all`      Delete all notes

------------------------------------------------------------------------

## 📝 Creating Notes

Create a note by passing content after `note add`:

``` bash
brain note add "Ship the CLI tool"
```

Or:

``` bash
brain note add Remember to refactor dispatch logic
```

Each time you create a note:

-   Storage is ensured at `~/.brain/notes`
-   A new numeric ID is generated
-   A markdown file is created automatically

Example file:

    ~/.brain/notes/3.md

File contents:

``` markdown
# Note 3

Ship the CLI tool
```

------------------------------------------------------------------------

## 🌳 Command Tree

Inspect the command structure with:

``` bash
brain tree
```

Example output:

    brain
    ├── help
    ├── tree
    ├── search    
    └── note
        ├── add
        ├── open
        ├── list
        ├── delete
        └── delete-all

------------------------------------------------------------------------

## 📂 Storage Location

All notes are stored locally at:

    ~/.brain/notes/

This directory is automatically created the first time you add a note.

There is:

-   No cloud storage
-   No external service
-   No database
-   No hidden state

Everything is just markdown files.

------------------------------------------------------------------------

## 🏗 Architecture Overview

brain is intentionally simple:

-   Uses `pathlib` for filesystem management
-   Uses a nested `COMMANDS` dictionary for routing
-   Uses a recursive `dispatch()` function
-   Generates incremental numeric note IDs
-   Prints command trees dynamically

This makes it easy to extend with new commands.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   `brain note append <id> <content>`

------------------------------------------------------------------------

Built with simplicity in mind.
