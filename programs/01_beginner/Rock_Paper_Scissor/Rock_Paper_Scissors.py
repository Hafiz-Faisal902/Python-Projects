import random


def RPS():
    choices = ["rock", "paper", "scissors"]
    print("=" * 40)
    print("Welcome to Rock Paper Scissors!")
    print("=" * 40)

    while True:
        # random.choice() picks one random item out of a list - this is
        # the computer's move for the round.
        computer_choice = random.choice(choices)
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        # The backslash (\) at the end of a line lets one logical
        # statement span several physical lines - this elif is really one
        # long condition, just written across three lines for readability.
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            continue
        elif choice == "no":
            print("Exiting RPS...")
            print("Thanks for playing! \nGoodbye.")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
            continue
