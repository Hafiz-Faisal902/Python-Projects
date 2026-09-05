"""
A command-line password generator.

Project #6 in the beginner track. Builds on the input-validation habits
from the earlier projects, but introduces a new and genuinely important
idea: not all randomness is equal.

`random` (used in Guess_Number and Rock_Paper_Scissors) is fine for games,
because nobody's security depends on guessing a number 1-50. But `random`
is *predictable* if you know its internal state - it was never designed
to resist someone trying to guess its output on purpose. Passwords need
the opposite guarantee, so this project uses the `secrets` module
instead, which Python's own documentation specifically recommends for
generating tokens, passwords, and anything else "security sensitive".
"""

import string
import secrets


def get_length() -> int:
    """Ask the user for a password length and validate it."""
    while True:
        try:
            length = int(input("Password length (minimum 4): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if length < 4:
            print("Length must be at least 4 for a password worth using.")
            continue

        return length


def get_character_pool() -> str:
    """
    Ask which character types to include, and combine the ones the user
    picks into a single string of allowed characters.

    Each yes/no question works the same way: keep asking until the answer
    is recognisably "yes" or "no", then only add that category's
    characters to the pool if the answer was yes.
    """
    categories = {
        "lowercase letters (a-z)": string.ascii_lowercase,
        "uppercase letters (A-Z)": string.ascii_uppercase,
        "digits (0-9)": string.digits,
        "symbols (!@#$...)": string.punctuation,
    }

    pool = ""
    for label, characters in categories.items():
        while True:
            answer = input(f"Include {label}? (yes/no): ").strip().lower()
            if answer in ("yes", "y"):
                pool += characters
                break
            elif answer in ("no", "n"):
                break
            else:
                print("Please answer 'yes' or 'no'.")

    # If the user said "no" to every single category, there's nothing to
    # build a password out of. Rather than crash later, catch it here and
    # ask again from the top.
    if not pool:
        print("\nYou need to include at least one character type.\n")
        return get_character_pool()

    return pool


def generate_password(length: int, pool: str) -> str:
    """
    Build a password by picking `length` random characters from `pool`.

    secrets.choice() picks one random item from a sequence, same as
    random.choice() - the difference is entirely in *how* that randomness
    is generated internally, not in how you call it. That's why swapping
    `random` for `secrets` here doesn't change the shape of the code at
    all, only its security guarantee.
    """
    return "".join(secrets.choice(pool) for _ in range(length))


def main() -> None:
    """Run the password generator application."""
    print("=" * 40)
    print("Welcome to the Password Generator!")
    print("=" * 40)

    while True:
        length = get_length()
        pool = get_character_pool()
        password = generate_password(length, pool)

        print(f"\nYour generated password:\n{password}\n")

        choice = input("Generate another password? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            print()
            continue
        elif choice in ("no", "n"):
            print("Exiting Password Generator...")
            print("Thanks for using the Password Generator! \nGoodbye.")
            break
        else:
            print("Invalid input. Exiting Password Generator...")
            break
