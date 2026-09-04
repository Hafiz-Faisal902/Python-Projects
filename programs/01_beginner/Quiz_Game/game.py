import random
import sys
import os
from quiz_data import quiz_categories
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



try:
    from quiz_data import quiz_categories
except ModuleNotFoundError:
    from programs.01_beginner.Quiz_Game.quiz_data import quiz_categories

def run_quiz():
    print("━" * 40)
    print("Welcome to the Ultimate Multi-Category Quiz!")
    print("━" * 40)

    # Outer loop to play multiple quizzes
    while True:
        print("\nSelect a Quiz Category:")
        for key, cat in quiz_categories.items():
            print(f"{key}. {cat['name']}")
        print("Q. Quit the program")

        # Get category choice
        choice = input("\nEnter your choice (1 - 20 or Q): ").strip().upper()

        if choice == "Q":
            print("\nThanks for playing! Goodbye.")
            break

        if choice not in quiz_categories:
            print("\nInvalid choice! Please select a valid category number.")
            continue

        # Get selected category data and shuffle questions
        selected_cat = quiz_categories[choice]
        quiz_data = selected_cat["questions"].copy()
        random.shuffle(quiz_data)

        score = 0
        total_questions = len(quiz_data)

        print(f"\nStarting Category: {selected_cat['name']}")
        print("━" * 40)

        # Loop through each question
        for index, data in enumerate(quiz_data, start=1):
            print(f"\nQuestion {index}: {data['question']}")
            for option in data["options"]:
                print(option)

            # Validate user input
            while True:
                user_guess = (
                    input("\nYour answer (A, B, C, or D): ").strip().upper()
                )
                if user_guess in ["A", "B", "C", "D"]:
                    break
                print("Invalid input! Please type A, B, C, or D.")

            # Check answer
            if user_guess == data["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {data['answer']}.")

        # Display final score for this round
        print("\n" + "━" * 40)
        print("Quiz Finished!")
        print(
            f"Your final score: {score}/{total_questions} ({(score / total_questions) * 100:.1f}%)"
        )
        print("━" * 40)

        # Ask if the user wants to play again
        play_again = (
            input("\nWould you like to play another quiz? (Y/N): ")
            .strip()
            .upper()
        )
        if play_again != "Y":
            print("\nThanks for playing! Goodbye.")
            break
