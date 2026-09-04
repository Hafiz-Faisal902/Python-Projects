"""
The Multi-Category Quiz Game.

Project #5 in the beginner track, and the biggest one so far - it pulls
20 categories worth of trivia out of quiz_data.py and turns them into a
proper multi-round quiz with scoring.
"""

import os
import random
import sys

# quiz_data.py lives in this same folder, so normally
# `from quiz_data import quiz_categories` would just work on its own. The
# one time it wouldn't is when this file gets loaded through the root
# launcher (main.py), since that script runs from the repo root, not from
# inside this folder - so this folder isn't automatically on Python's
# search path yet.
#
# Adding this folder to sys.path ourselves, before the import, makes
# `import quiz_data` work reliably no matter how game.py was started:
# directly, or through the root menu.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quiz_data import quiz_categories


def run_quiz():
    print("━" * 40)
    print("Welcome to the Ultimate Multi-Category Quiz!")
    print("━" * 40)

    # Outer loop: lets the player pick a new category and go again after
    # finishing one, without restarting the whole program.
    while True:
        print("\nSelect a Quiz Category:")
        # quiz_categories is a dictionary of dictionaries - each key is a
        # category number, each value holds that category's name and its
        # question list. .items() lets us loop over the key and value
        # together instead of looking each one up separately.
        for key, cat in quiz_categories.items():
            print(f"{key}. {cat['name']}")
        print("Q. Quit the program")

        choice = input("\nEnter your choice (1 - 20 or Q): ").strip().upper()

        if choice == "Q":
            print("\nExiting Quiz Game...")
            print("Thanks for playing! Goodbye.")
            break

        if choice not in quiz_categories:
            print("\nInvalid choice! Please select a valid category number.")
            continue

        # .copy() matters here: without it, quiz_data would just be
        # another name pointing at the *same* list stored in
        # quiz_categories, and shuffling it would permanently scramble the
        # original question order for every future round too.
        selected_cat = quiz_categories[choice]
        quiz_data = selected_cat["questions"].copy()
        random.shuffle(quiz_data)

        score = 0
        total_questions = len(quiz_data)

        print(f"\nStarting Category: {selected_cat['name']}")
        print("━" * 40)

        # enumerate(quiz_data, start=1) hands us a running counter
        # (starting at 1 instead of 0) alongside each question dictionary
        # - handy for printing "Question 1", "Question 2", and so on.
        for index, data in enumerate(quiz_data, start=1):
            print(f"\nQuestion {index}: {data['question']}")
            for option in data["options"]:
                print(option)

            # A small inner loop purely for input validation: keep asking
            # until the player types exactly A, B, C, or D.
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
            print("\nExiting Quiz Game...")
            print("Thanks for playing! Goodbye.")
            break
