import importlib


Calculator = getattr(importlib.import_module("programs.01_beginner.Calculator.Calculator"), "Calculator")
Guess_Number = getattr(importlib.import_module("programs.01_beginner.Guess_Number.Guess_Number"), "Guess_Number")
RPS = getattr(importlib.import_module("programs.01_beginner.Rock_Paper_Scissor.Rock_Paper_Scissors"), "RPS")
To_Do_List = getattr(importlib.import_module("programs.01_beginner.To_Do_List.To_Do_List"), "main")


while True:
    print("\n===== Main Menu =====")
    print("Available options:")
    print("1. Calculator")
    print("2. Guess Number")
    print("3. Rock Paper Scissors")
    print("4. To Do List")
    print("5. Exit")
    print("6. Help")
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

    elif userplay == "1":
        print("Starting the Calculator...")
        Calculator()

    elif userplay == "2":
        print("Starting the Guess Number...")
        Guess_Number()

    elif userplay == "3":
        print("Starting the Rock Paper Scissors...")
        RPS()

    elif userplay == "4":
        print("Starting the To Do List...")
        To_Do_List()

    else:
        print("Game not found. Please choose a valid option from the menu or type help.")
