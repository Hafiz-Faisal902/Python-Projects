"""
A simple command-line calculator.

This is Project #1 in the beginner track. The goal isn't to build
something fancy - it's to get comfortable with the four things you'll use
in almost every Python program: reading input, branching with
if/elif/else, looping with while, and printing output.
"""


def Calculator():
    print("=" * 40)
    print("Welcome to the Calculator!")
    print("=" * 40)

    # while True loops forever until something inside it hits `break`.
    # Our only exit is at the bottom, when the user answers "no" to
    # "calculate again?".
    while True:
        # input() always returns a string, even if someone types numbers.
        # int() converts that string into a real integer so we can do math
        # with it.
        #
        # Heads up: this will crash with a ValueError if someone types
        # something that isn't a whole number, like "3.5" or "abc". We're
        # leaving that as-is on purpose - handling it is basically the
        # next lesson. Take a look at how Guess_Number.py wraps its
        # input() in a try/except, and try adding the same idea here.
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()

        # A plain if/elif/else chain: Python checks each condition top to
        # bottom and runs the first one that matches.
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            # Dividing by zero would crash the program with a
            # ZeroDivisionError, so we check for it ourselves first and
            # print a friendly message instead of letting Python explode.
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operator!")

        # .strip() clears accidental leading/trailing spaces (" yes ") and
        # .lower() makes the check case-insensitive, so "Yes", "YES", and
        # "yes" all count as the same answer.
        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice == "yes":
            continue
        elif choice == "no":
            print("Exiting Calculator...")
            print("Thanks for using the Calculator! \nGoodbye.")
            break
        else:
            print("Invalid input\nPlease enter 'yes' or 'no'.")
