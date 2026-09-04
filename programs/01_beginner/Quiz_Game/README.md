# Quiz Game

**Project #5** in the beginner track, and the biggest one in Phase 1 by a wide margin.

A multi-category trivia game. Pick a category, answer a set of multiple-choice questions in random order, and get a score at the end. I kept adding categories while building this one because it turned out to be genuinely fun to write trivia questions — it started as "Python Basics" and ended up at 20 categories covering programming, science, history, geography, and a few random ones like personal finance and everyday health.

## What it does

- Shows a menu of 20 quiz categories, from Python and JavaScript to World Capitals and Ancient History
- Shuffles the question order every time you play a category, so it doesn't get repetitive
- Validates your answer input (only A, B, C, or D count)
- Scores you at the end as a fraction and a percentage
- Lets you jump straight into another category, or quit whenever

## Files in this folder

```text
Quiz_Game/
├── game.py         # The quiz loop, scoring, and menu logic
├── quiz_data.py     # All 20 categories and their questions — just data, no logic
├── main.py          # Entry point for running this project on its own
└── README.md
```

Keeping the questions in `quiz_data.py`, separate from the game logic in `game.py`, means adding a new category is just adding a new dictionary entry — no need to touch the actual game code. `quiz_data.py` has a comment at the top showing the exact shape to copy if you want to add your own.

## Concepts practiced

- Dictionaries of dictionaries, and looping over them with `.items()`
- `random.shuffle()` — and why you shuffle a `.copy()` of the list, not the original
- `enumerate(..., start=1)` for numbering questions from 1 instead of 0
- A validation loop nested inside the main game loop (for the answer input)
- Splitting data (`quiz_data.py`) from logic (`game.py`) across files
- `sys.path` — this project's own `main.py` and the repo's root launcher both need to reach `quiz_data.py`, and `game.py` handles that by adding its own folder to `sys.path` before importing

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 5
```

## Example

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Welcome to the Ultimate Multi-Category Quiz!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Select a Quiz Category:
1. Python Basics
2. General Tech
...
20. World War II Trivia
Q. Quit the program

Enter your choice (1 - 20 or Q): 1

Starting Category: Python Basics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Question 1: Which keyword is used to create a function in Python?

A. define
B. function
C. fun
D. def

Your answer (A, B, C, or D): D
Correct!
```

## Ideas for later

- Save high scores to a file so they survive between runs
- A timer per question, for a "rapid fire" mode
- Load categories from a `.json` file instead of a hardcoded dictionary — good practice for Phase 2
