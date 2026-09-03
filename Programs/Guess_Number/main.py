import random


def Guess_Number():
    Guessnum = random.randint(1, 50)
        
    while True:
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
            break
        elif num > Guessnum:
            print("Lower number please...")
        elif num < Guessnum:
            print("Higher number please...")