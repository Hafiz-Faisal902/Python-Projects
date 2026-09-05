"""
Central launcher for the Python Projects repo.

Instead of a normal `import` for every mini project, this file uses
importlib.import_module() and passes the module path in as a plain
string. That's not just a style choice - it's actually required here,
because the folder is named "01_beginner", and a name that starts with a
digit is not a valid Python identifier. You genuinely cannot write
`from programs.01_beginner.Calculator import Calculator` - the parser
throws a SyntaxError before your code even runs, because it tries to read
"01" as the start of a number.

importlib.import_module() sidesteps that completely, because it takes the
path as a *string*, built at runtime, instead of literal syntax the
parser has to validate. Strings can contain whatever characters they want.
"""

import importlib

# getattr(module, "name") does the same job as module.name, just
# dynamically. Each line below imports one project's module, then
# immediately grabs the single function (or class) that actually starts
# it, storing it under a short, friendly name.
Calculator = getattr(importlib.import_module("programs.01_beginner.Calculator.Calculator"), "Calculator")
Guess_Number = getattr(importlib.import_module("programs.01_beginner.Guess_Number.Guess_Number"), "Guess_Number")
RPS = getattr(importlib.import_module("programs.01_beginner.Rock_Paper_Scissor.Rock_Paper_Scissors"), "RPS")
To_Do_List = getattr(importlib.import_module("programs.01_beginner.To_Do_List.To_Do_List"), "main")
run_quiz = getattr(importlib.import_module("programs.01_beginner.Quiz_Game.game"), "run_quiz")
generate_password = getattr(importlib.import_module("programs.01_beginner.Password_Generator.Password_Generator"), "main")
start_countdown = getattr(importlib.import_module("programs.01_beginner.Countdown_Timer.Countdown_Timer"), "main")


# The main menu loop. while True keeps showing the menu until the user
# types "exit" (or hits Ctrl+C). Picking a number just calls that
# project's own function - control comes back here once that project's
# own loop finishes.
while True:
    print("\n===== Main Menu =====")
    print("Available options:")
    print("1. Calculator")
    print("2. Guess Number")
    print("3. Rock Paper Scissors")
    print("4. To Do List")
    print("5. Quiz Game")
    print("6. Password Generator")
    print("7. Countdown Timer")
    print("Exit or Help for more options.")
    userplay = input("Which game do you want to play? ").strip().lower()

    if userplay == "exit":
        print("Exiting the program...")
        print("Thanks for playing! Goodbye.")
        break

    elif userplay == "help":
        print("\n===== Help Menu =====")
        print("Available options: Calculator, Guess Number, Rock Paper Scissors, To Do List, Quiz Game, Password Generator, Countdown Timer, Exit, Help")
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

    elif userplay == "5":
        print("Starting the Quiz Game...")
        run_quiz()

    elif userplay == "6":
        print("Starting the Password Generator...")
        generate_password()

    elif userplay == "7":
        print("Starting the Countdown Timer...")
        start_countdown()

    else:
        print("Game not found. Please choose a valid option from the menu or type help.")
