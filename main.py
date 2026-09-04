import importlib


Calculator = getattr(importlib.import_module("programs.01_beginner.Calculator.Calculator"), "Calculator")
Guess_Number = getattr(importlib.import_module("programs.01_beginner.Guess_Number.Guess_Number"), "Guess_Number")
RPS = getattr(importlib.import_module("programs.01_beginner.Rock_Paper_Scissor.Rock_Paper_Scissors"), "RPS")


while True:
    print("\n===== Main Menu =====")
    print("Available options:")
    print("1. Calculator")
    print("2. Guess Number")
    print("3. Rock Paper Scissors")
    print("4. Exit")
    print("5. Help")
    userplay = input("Which game do you want to play? ").strip().lower()

    if userplay == "exit":
        print("Exiting the program...")
        print("Thanks for playing! Goodbye.")
        break

    elif userplay == "help":
        print("\n===== Help Menu =====")
        print("Available options: Calculator, Guess Number, Exit, Help")
        print("Type the name of the game you want to play or 'exit' to quit.")
        print("You can also play any specific game by going in the directory.")

    elif userplay == "calculator":
        print("Starting the Calculator...")
        Calculator()

    elif userplay == "guess number":
        print("Starting the Guess Number...")
        Guess_Number()

    elif userplay == "rock paper scissors":
        print("Starting the Rock Paper Scissors...")
        RPS()

    else:
        print("Game not found. Please choose a valid option from the menu or type help.")
