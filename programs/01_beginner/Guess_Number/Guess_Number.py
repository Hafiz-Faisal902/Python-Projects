import random


def Guess_Number():
    # random.randint(1, 50) picks a random whole number from 1 to 50,
    # both ends included. This is the number the player is trying to find.
    Guessnum = random.randint(1, 50)
    print("=" * 40)
    print("Welcome to the Guess Number Game!")
    print("=" * 40)

    while True:
        # try/except is how Python handles errors without crashing the
        # whole program. int(input(...)) raises a ValueError if the text
        # typed in isn't a whole number (like "twelve" or "5.5"). Catching
        # that here means a bad guess just asks again instead of ending
        # the game.
        try:
            num = int(input("Guess a number (1-50): "))
        except ValueError:
            print("Invalid input! Please enter a valid number, not text.")
            continue

        if num < 1 or num > 50:
            print("Invalid number! Please choose between 1 and 50.")
            continue

        if num == Guessnum:
            print("Congratulations, you guessed the number.")
            choice = input("Do you want to try again? (yes/no): ").strip().lower()
            if choice == "yes":
                # Pick a brand new number for the next round. Without this
                # line, "playing again" would just ask you to re-guess the
                # exact number you already found.
                Guessnum = random.randint(1, 50)
                continue
            elif choice == "no":
                print("Exiting Guess Number Game...")
                print("Thanks for playing! \nGoodbye.")
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
        elif num > Guessnum:
            print("Lower number please...")
        elif num < Guessnum:
            print("Higher number please...")
