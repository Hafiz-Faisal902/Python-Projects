# Countdown Timer

**Project #7** in the beginner track.

A command-line countdown that ticks down from a minutes-and-seconds duration you choose, updating a single line in place instead of scrolling the screen full of timestamps.

## What it does

- Asks for minutes and seconds separately (seconds capped at 0-59, so "90 seconds" has to be entered as 1:30)
- Rejects a 0:00 duration
- Counts down in real time, redrawing the same line each second
- Prints "Time's up!" when it reaches zero
- Loops so you can start another countdown without restarting the program

## Concepts practiced

- The `time` module — `time.sleep(1)` for a genuine, real-world one-second pause (not just a fast loop)
- Updating one line of terminal output in place with `print(..., end="\r", flush=True)`, instead of printing a new line every tick
- `divmod()` for turning a total second count into minutes + leftover seconds in one step
- Format spec `:02d` for zero-padded numbers, so the display reads like a real clock (`00:09`, not `0:9`)
- Splitting related input validation into two small, near-identical functions (`get_minutes`, `get_seconds`) rather than one that tries to do both

## Why minutes and seconds as two separate inputs

The alternative — one prompt for "total seconds" — is simpler to code, but it skips a small, useful piece of practice: taking two related numbers, validating each one under its own rules (minutes just can't be negative; seconds specifically can't exceed 59), and combining them yourself (`minutes * 60 + seconds`) before the real logic even starts. It's a preview of a pattern that shows up constantly in bigger programs — collecting several pieces of raw input, then normalizing them into the one number the rest of the code actually needs.

## What it doesn't do (yet)

- **Can't be interrupted cleanly.** Hitting Ctrl+C mid-countdown exits with a raw `KeyboardInterrupt` traceback instead of a friendly message. Catching that (`except KeyboardInterrupt:`) and exiting gracefully is a good exercise once exception handling feels comfortable.
- **No sound.** A cross-platform "beep" when the timer finishes needs either a platform-specific system call or an external library — not worth pulling in a dependency for a Tier 1 project, but a reasonable addition if this gets revisited later with `playsound` or similar.

## Run it

From inside this folder:

```bash
python main.py
```

Or from the repo root, through the launcher:

```bash
python main.py
# then choose option 7
```

## Example

```text
========================================
Welcome to the Countdown Timer!
========================================
Minutes: 0
Seconds (0-59): 5

Starting countdown from 00:05...

00:00

Time's up!

Start another countdown? (yes/no): no
Exiting Countdown Timer...
Thanks for using the Countdown Timer!
Goodbye.
```

(In a real terminal, `00:05` through `00:00` appear as the *same line* updating each second — this README just can't show that motion in plain text.)
