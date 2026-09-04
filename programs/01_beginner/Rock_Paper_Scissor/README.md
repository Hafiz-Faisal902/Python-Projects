# Rock Paper Scissors

**Project #3** in the beginner track.

The standard game, played against the computer in the terminal. Nothing complicated — pick one of three options, compare it against a random computer pick, and see who wins. It's mostly here to practice comparing multiple conditions cleanly instead of writing a wall of nested `if` statements.

## What it does

- Picks a random move for the computer each round
- Compares it against your move and prints who won
- Rejects anything that isn't `rock`, `paper`, or `scissors`
- Loops for as many rounds as you want

## Concepts practiced

- `random.choice()` to pick from a list
- Combining multiple conditions with `and` / `or` in one `elif`
- Splitting one long condition across multiple lines with `\` for readability
- Membership checks with `in` (`if user_choice not in choices`)

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 3
```

## Example

```text
========================================
Welcome to Rock Paper Scissors!
========================================
Enter rock, paper, or scissors: rock
Computer chose: scissors
You win!
Do you want to play again? (yes/no): no
Exiting RPS...
Thanks for playing!
Goodbye.
```
