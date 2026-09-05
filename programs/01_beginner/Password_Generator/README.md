# Password Generator

**Project #6** in the beginner track.

A command-line tool that builds random passwords from character types you choose (lowercase, uppercase, digits, symbols) at a length you choose. Structurally, this is the first project written entirely as small functions from the start, following the pattern `To_Do_List` introduced — no single giant function doing everything.

## What it does

- Asks for a password length (minimum 4)
- Lets you toggle which character types to include
- Generates a password using those choices
- Loops so you can generate as many as you want in one session

## Concepts practiced

- Splitting a program into small, single-purpose functions from the start
- Looping input validation until the answer is actually usable
- Dictionaries used to pair a human-readable label with its matching data (`categories`)
- Generator expressions (`secrets.choice(pool) for _ in range(length)`)
- Recursion as a clean way to "start a step over" (`get_character_pool()` calling itself if nothing was selected)

## Why `secrets` instead of `random`

Every earlier project in this repo (`Guess_Number`, `Rock_Paper_Scissors`) uses Python's `random` module, and that's the right choice for a game — nobody's security depends on it. A password is different: if it needs to resist an attacker who's specifically trying to guess it, the *quality* of the randomness matters, not just its unpredictability at a glance.

`random` is a [Mersenne Twister](https://docs.python.org/3/library/random.html#random.random) — deterministic and, in principle, predictable if enough of its output is observed. It's explicitly **not** intended for security purposes; the Python docs say so directly. `secrets` exists specifically to fix that: it pulls from the operating system's cryptographically secure random source instead.

The interesting part is that the code barely changes — `secrets.choice()` has the exact same signature as `random.choice()`. The lesson here isn't new syntax, it's picking the right tool for what the code is actually protecting.

## What it doesn't do (yet)

- No guarantee that the password contains at least one character from *every* selected category — a 12-character password built from "letters + digits" could technically come back all letters, just by chance. Fixing that (e.g., forcing one character per selected type, then filling the rest randomly and shuffling) is a good exercise once loops and lists feel comfortable.
- No strength meter or estimated crack-time feedback — that's a reasonable feature for a later, more advanced revisit of this idea.

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 6
```

## Example

```text
========================================
Welcome to the Password Generator!
========================================
Password length (minimum 4): 12
Include lowercase letters (a-z)? (yes/no): yes
Include uppercase letters (A-Z)? (yes/no): yes
Include digits (0-9)? (yes/no): yes
Include symbols (!@#$...)? (yes/no): yes

Your generated password:
(clA>2u<!9=p

Generate another password? (yes/no): no
Exiting Password Generator...
Thanks for using the Password Generator!
Goodbye.
```
