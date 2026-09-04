# To-Do List

A small command-line to-do list. **Project #4** in the beginner track.

## What it does

The program lets you:

- Add tasks
- View current tasks
- Complete tasks (which removes them from the list)
- Exit the program

Every menu option also accepts a plain word instead of the number — `add`, `view`, `complete`, `exit` all work, not just `1`–`4`.

Tasks are kept in memory while the program is running. They are intentionally **not saved to a file yet** — persistent storage gets introduced later, once file handling is part of the learning progression. Restart the program and the list is gone; that's expected for now, not a bug.

## Concepts practiced

- Lists
- Functions
- `while` loops
- `if` / `elif` / `else`
- User input
- String cleaning with `strip()` and `lower()`
- Basic validation
- `try` / `except`
- `enumerate()`

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 4
```

## Example

```text
===== To-Do List =====
1. Add task
2. View tasks
3. Complete task
4. Exit
Choose an option: add
Enter a task: Finish the To-Do List README
Task added.

===== To-Do List =====
1. Add task
2. View tasks
3. Complete task
4. Exit
Choose an option: view

===== Your Tasks =====
1. Finish the To-Do List README

===== To-Do List =====
1. Add task
2. View tasks
3. Complete task
4. Exit
Choose an option: complete

===== Your Tasks =====
1. Finish the To-Do List README
Enter the task number to complete: 1
Completed: Finish the To-Do List README
```
