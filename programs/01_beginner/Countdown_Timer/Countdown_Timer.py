"""
A command-line countdown timer.

Project #7 in the beginner track. Introduces two new ideas: the `time`
module for actually waiting in real time, and updating a single line of
output in place instead of printing a new line every second.
"""

import time


def get_minutes() -> int:
    """Ask for the minutes part of the countdown and validate it."""
    while True:
        try:
            minutes = int(input("Minutes: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minutes < 0:
            print("Minutes can't be negative.")
            continue

        return minutes


def get_seconds() -> int:
    """
    Ask for the seconds part of the countdown and validate it.

    This is deliberately capped at 59, not left open-ended - "90 seconds"
    should be entered as 1 minute 30 seconds, not 0 minutes 90 seconds.
    Keeping the two inputs in their normal ranges makes the countdown
    display (`mm:ss`) behave the way anyone reading a clock would expect.
    """
    while True:
        try:
            seconds = int(input("Seconds (0-59): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if seconds < 0 or seconds > 59:
            print("Seconds must be between 0 and 59.")
            continue

        return seconds


def countdown(total_seconds: int) -> None:
    """
    Count down from `total_seconds` to zero, updating one line in place.

    Normally, print() ends every call with a newline, so each call starts
    a fresh line. Passing `end="\\r"` instead replaces that newline with a
    carriage return, which moves the cursor back to the start of the
    *current* line rather than advancing to a new one - so the next
    print() overwrites what's already there instead of stacking below it.
    `flush=True` matters here too: normally Python buffers output until
    there's a newline, which would make everything wait to appear until
    the whole countdown finished. Flushing forces each line out
    immediately, so the countdown actually looks like it's ticking down
    in real time instead of printing all at once at the end.
    """
    while total_seconds >= 0:
        # divmod(total_seconds, 60) does one division and gets both the
        # quotient (whole minutes) and the remainder (leftover seconds)
        # in a single step, instead of writing that as two separate
        # calculations.
        minutes, seconds = divmod(total_seconds, 60)

        # The :02d format spec pads a number with a leading zero if it's
        # only one digit - so 5 becomes "05" instead of "5", keeping the
        # display looking like a real clock (05:09, not 5:9).
        print(f"\r{minutes:02d}:{seconds:02d}", end="", flush=True)

        if total_seconds == 0:
            break

        time.sleep(1)
        total_seconds -= 1

    # A real newline here, not another \r - this is the last thing
    # printed, so it should stay on its own line instead of getting
    # overwritten by the message that comes right after it.
    print("\n\nTime's up!")


def main() -> None:
    """Run the countdown timer application."""
    print("=" * 40)
    print("Welcome to the Countdown Timer!")
    print("=" * 40)

    while True:
        minutes = get_minutes()
        seconds = get_seconds()
        total_seconds = (minutes * 60) + seconds

        if total_seconds == 0:
            print("A 0-second countdown isn't much of a timer. Try again.\n")
            continue

        print(f"\nStarting countdown from {minutes:02d}:{seconds:02d}...\n")
        countdown(total_seconds)

        choice = input("\nStart another countdown? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            print()
            continue
        elif choice in ("no", "n"):
            print("Exiting Countdown Timer...")
            print("Thanks for using the Countdown Timer! \nGoodbye.")
            break
        else:
            print("Invalid input. Exiting Countdown Timer...")
            break
