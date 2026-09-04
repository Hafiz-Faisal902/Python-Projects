# Guess the Number

**Project #2** in the beginner track.

A classic higher/lower guessing game. The program picks a random number between 1 and 50, and you keep guessing until you land on it. This one's small, but it's the first project in the repo that actually validates input properly instead of letting a bad guess crash the program.

## What it does

- Picks a random secret number from 1–50
- Tells you to guess higher or lower after each wrong guess
- Rejects non-numbers and out-of-range guesses without crashing
- Lets you play again — and yes, it actually picks a *new* number each time (an earlier version of this didn't, so "play again" just asked you to re-guess a number you'd already found)

## Concepts practiced

- `random.randint()` for picking the secret number
- `try` / `except ValueError` — actually handling bad input instead of crashing
- Nested `if` conditions for the higher/lower/correct logic
- Loop control with `continue` and `break`

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 2
```

## Example

```text
========================================
Welcome to the Guess Number Game!
========================================
Guess a number (1-50): 25
Lower number please...
Guess a number (1-50): 12
Higher number please...
Guess a number (1-50): 18
Congratulations, you guessed the number.
Do you want to try again? (yes/no): no
Exiting Guess Number Game...
Thanks for playing!
Goodbye.
```
