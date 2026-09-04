# Multi-Category Quiz Game

A modular, CLI-driven interactive trivia engine designed to test a player's knowledge across multiple academic, technical, and general lifestyle categories. 

This project demonstrates core backend engineering foundations in Python, featuring structured data validation, automated collection shuffling, cross-file imports, and localized game loop configurations.

## Features

- **Categorized Playlists:** Offers a diverse catalog of topics spanning from technical fields (Python, JavaScript, Data Structures) to everyday knowledge (Finance, First Aid, History, and Math).
- **Dynamic Replay Engine:** Wrapped in an structural `while` loop that allows players to seamlessly pivot to alternative topics or restart rounds without terminating the program execution.
- **Non-Linear Questioning:** Uses random seed algorithms to copy and shuffle question sets per session, guaranteeing a fresh sequence during every gameplay cycle.
- **Input Sanitization:** Features a continuous validation barrier that filters user entry anomalies and rejects out-of-bounds variations cleanly.
- **Adaptive Performance Metrics:** Calculates precise execution summaries and prints a live percentage-based score upon completion.

## Directory Structure

The project separates the logic controller from the raw content schemas to adhere to clean configuration principles:

```text
Quiz_Game/
├── game.py          # Central quiz orchestrator, data loop, and CLI controller
├── quiz_data.py     # Structural dictionary data layout housing categories and lists
└── README.md        # Documentation profile
```

## System Requirements

- **Python Runtime:** Python 3.6 or higher
- **External Dependencies:** None (Utilizes standard library allocations only)

## Execution

### Run Directly
To launch the quiz game independently from your terminal shell, run:

```bash
python programs/01_beginner/Quiz_Game/game.py
```

### Run via Root Launcher
Alternatively, this project is fully integrated into the repository's root management node. Execute the primary environment wrapper and select option `5`:

```bash
python main.py
```

## Schema Configuration Blueprint

The underlying content system relies on a structural mapping algorithm. New categories can be appended instantly by scaling the key sequence inside `quiz_data.py`:

```python
"CATEGORY_ID": {
    "name": "Category Human Title",
    "questions": [
        {
            "question": "Your targeted text interrogation statement?",
            "options": ["\nA. Option 1", "\nB. Option 2", "\nC. Option 3", "\nD. Option 4"],
            "answer": "CORRECT_LETTER_KEY"
        }
    ]
}
```

## Future Roadmap Modifications

- Add a structural history parser to export high scores into a local text database (`scores.txt`).
- Implement an automated time-delta countdown mechanism per question to simulate rapid-fire testing constraints.
- Build a custom input parser to allow loading quiz modules straight from a localized `.json` file pipeline.
