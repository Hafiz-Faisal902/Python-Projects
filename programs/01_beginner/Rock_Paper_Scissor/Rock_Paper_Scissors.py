import random

def RPS():
    choices = ["rock", "paper", "scissors"]
    print("\n===== Rock Paper Scissors Game =====")
    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == "yes": 
            continue
        elif choice == "no".strip().lower():
            print("Exiting RPS...")
            print("Thanks for playing! \nGoodbye.")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
            continue

