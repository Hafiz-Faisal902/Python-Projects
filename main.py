from Programs.Calculator.main import Calculator
from Programs.Guess_Number.main import Guess_Number

while True:
    print("\n--- Main Menu ---")
    print("Available options: Calculator, Guess Number, Exit, Help")
    userplay = input("Which game do you want to play? ").strip().lower()

    if userplay == "exit":
        print("Thanks for playing! Goodbye.")

    elif userplay == "help":
        print("Available options: Calculator, Guess Number, Exit, Help")
        print("Type the name of the game you want to play or 'exit' to quit.")

    elif userplay == "calculator".strip().lower():
        Calculator()

    elif userplay == "guess number".strip().lower():
        Guess_Number()

    elif userplay == "rock paper scissors".strip().lower():
        Rock_Paper_Scissors()

    else:
        print("Game not found. Please choose a valid option from the menu or type help.")
