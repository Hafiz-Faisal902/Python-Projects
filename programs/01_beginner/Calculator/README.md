# Calculator

**Project #1** in the beginner track.

A command-line calculator that does the four basic operations and keeps going until you tell it to stop. It's the "hello world" of this repo — simple on purpose, so the loop/branch/input pattern used everywhere else in this project has somewhere easy to start.

## What it does

- Takes two numbers and an operator (`+`, `-`, `*`, `/`)
- Prints the result
- Catches division by zero instead of crashing
- Asks if you want to go again, and loops until you say no

## What it doesn't do (yet)

If you type something that isn't a whole number, it'll crash with a `ValueError` instead of asking again — there's no `try`/`except` around the number input here on purpose. `Guess_Number` (project #2) shows the fix for that; recreating it here is a good exercise if you want one.

## Concepts practiced

- `while` loop as the main program loop
- `if` / `elif` / `else` chains
- Basic arithmetic and integer conversion (`int(input(...))`)
- Guarding against a specific runtime error (division by zero)
- `.strip().lower()` for forgiving yes/no input

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 1
```

## Example

```text
========================================
Welcome to the Calculator!
========================================
Enter first number: 10
Enter second number: 4
Enter operator (+, -, *, /): *
40
Do you want to perform another calculation? (yes/no): no
Exiting Calculator...
Thanks for using the Calculator!
Goodbye.
```
