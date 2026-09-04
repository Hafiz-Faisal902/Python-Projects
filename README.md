# Python Projects

This is where I'm learning Python by actually building things instead of just following along with tutorials. Every folder in here is a small, complete program — no half-finished snippets — and each one is a little harder than the last.

The idea is simple: start with plain console programs and basic logic, and work up toward bigger stuff (files, databases, OOP, maybe even some automation and AI-related projects later on) as the skills stack up. Nothing here is meant to be "finished" forever — it's a running log of what I've built and what I understood well enough to actually ship.

## How the repo is laid out

```text
Python-Projects/
├── main.py                          # Menu that launches any project from one place
├── LICENSE
└── programs/
    └── 01_beginner/
        ├── Calculator/
        ├── Guess_Number/
        ├── Rock_Paper_Scissor/
        ├── To_Do_List/
        └── Quiz_Game/
```

Every project folder is self-contained: its own game/logic file, its own `main.py` to run it, and its own `README.md` explaining what it does and what it's practicing. `programs/01_beginner/` is the only tier that exists right now — it's Phase 1. More folders (`02_beginner-intermediate`, `03_intermediate`, and so on) will show up as I actually get there, not before. I'd rather the repo reflect what's really built than promise a roadmap I haven't earned yet.

## Running things

**Option 1 — the menu launcher.** Run this from the repo root and pick a number:

```bash
python main.py
```

**Option 2 — run a project on its own.** Every project also works standalone from inside its own folder:

```bash
cd programs/01_beginner/Quiz_Game
python main.py
```

No installs, no virtual environment, no `requirements.txt` — everything here so far only uses Python's standard library (`random`, mainly). That'll change once I start doing anything with APIs or file parsing, and I'll update this when it does.

## The projects so far

| # | Project | What it is |
|---|---------|------------|
| 1 | [Calculator](programs/01_beginner/Calculator) | Basic arithmetic on two numbers, loops until you're done |
| 2 | [Guess Number](programs/01_beginner/Guess_Number) | Classic higher/lower guessing game against a random number |
| 3 | [Rock Paper Scissors](programs/01_beginner/Rock_Paper_Scissor) | You vs. the computer, best of however-many-rounds you want |
| 4 | [To-Do List](programs/01_beginner/To_Do_List) | Add, view, and complete tasks (in-memory only, for now) |
| 5 | [Quiz Game](programs/01_beginner/Quiz_Game) | Multi-category trivia — 20 categories, random question order, scored |

Each link goes to that project's own README with more detail on how it works and what it's teaching me.

## What Phase 1 was actually about

Nothing exotic — just getting the fundamentals to feel automatic:

- `while` loops for "keep going until the user is done"
- `if` / `elif` / `else` branching
- reading and validating user input (and not crashing when someone types nonsense)
- `try` / `except` for the inputs that genuinely need it
- lists, dictionaries, and looping over both
- writing small functions instead of one giant script
- splitting a project into a "logic" file and a `main.py` entry point

## A couple of things I learned the hard way

Two of these projects broke in slightly annoying ways that taught me more than the parts that worked first try:

- **A folder can't start with a digit and still be `import`-able the normal way.** `programs/01_beginner/` can't be reached with a plain `from programs.01_beginner.X import Y` — Python's parser reads `01` as the start of a number and throws a `SyntaxError` before your code even runs. That's why `main.py` at the root uses `importlib.import_module()` instead: it takes the module path as a plain string at runtime, so it doesn't care that the folder name isn't a "valid" identifier.
- **A project's own `main.py` doesn't automatically know about its neighbors.** Each project folder works standalone because Python adds a script's own directory to its search path automatically — but only *that* directory. Anything that needs to reach outside its own folder (like `Quiz_Game/game.py` pulling in `quiz_data.py` when launched through the root menu) needs to add that folder to `sys.path` itself first.

## What's next

Once Phase 1 feels solid, Phase 2 is about giving these projects actual memory — saving the to-do list to a file, loading quiz questions from JSON instead of a hardcoded dictionary, that kind of thing. After that: `sqlite3`, proper OOP structure, and eventually some small automation/AI projects. I'll add the folders when there's real code in them, not before.

## License

MIT — see [LICENSE](LICENSE). Use it, learn from it, fork it.
