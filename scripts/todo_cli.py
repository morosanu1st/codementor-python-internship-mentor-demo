#!/usr/bin/env python3
"""Minimal todo CLI — practice argparse, lists, and file I/O."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "todos.json"


def load_todos() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_todos(todos: list[dict]) -> None:
    DATA_FILE.write_text(json.dumps(todos, indent=2), encoding="utf-8")


def cmd_add(text: str) -> None:
    todos = load_todos()
    todos.append({"id": len(todos) + 1, "text": text, "done": False})
    save_todos(todos)
    print(f"Added: {text}")


def cmd_list() -> None:
    todos = load_todos()
    if not todos:
        print("No todos yet.")
        return
    for t in todos:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}: {t['text']}")


def cmd_done(todo_id: int) -> None:
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"Done: {t['text']}")
            return
    print(f"No todo with id {todo_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Tiny todo CLI for Python practice")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Add a todo")
    add_p.add_argument("text")

    sub.add_parser("list", help="List todos")

    done_p = sub.add_parser("done", help="Mark a todo done")
    done_p.add_argument("id", type=int)

    args = parser.parse_args()
    if args.command == "add":
        cmd_add(args.text)
    elif args.command == "list":
        cmd_list()
    elif args.command == "done":
        cmd_done(args.id)


if __name__ == "__main__":
    main()
