# 🚀 Python Projects: Learning Sandbox

A hand-crafted, production-style sandbox repository built one modular application at a time. 

The core goal of this environment is to transition methodically from console prototypes up to advanced software architectures, automated pipelines, and localized AI models—maintaining structural data validation, clean documentation, and strict engineering discipline at every milestone.

---

## 🛠️ Repository Architecture

The project utilizes a centralized workspace launcher node (`main.py`) paired with isolated module pools split by target difficulty:

```text
Python-Projects/
├── main.py                     # Central ecosystem launcher & routing hub
├── requirements.txt            # System dependencies (when applicable)
├── programs/                   # Core application codebase split by tier
│   ├── 01_beginner/
│   │   ├── Calculator/         # Operational mathematical sandbox
│   │   ├── Guess_Number/       # Low/High predictive logic game
│   │   ├── Rock_Paper_Scissor/ # Algorithmic choice matrix engine
│   │   ├── To_Do_List/         # CRUD-style local memory task master
│   │   └── Quiz_Game/          # Multi-category trivia engine with modular datasets
│   ├── 02_beginner-intermediate/
│   ├── 03_intermediate/
│   ├── 04_advanced/
│   ├── 05_ai-automation/
│   └── 06_professional/
└── docs/                       # Technical briefs and deep-dives
```

---

## 🏎️ Quick Start & Execution

You can run individual modules raw from your shell or use the global terminal dispatcher node.

### Option A: The Central Launcher (Recommended)
Boot the main command-line interface to pivot dynamically between available applications without restarting your process environment:

```bash
python main.py
```

### Option B: Direct Script Targeting
Execute any isolated application script directly from your terminal workspace:

```bash
# Example: Deploying the automated Quiz Game engine directly
python programs/01_beginner/Quiz_Game/game.py
```

---

## 📈 Development Tracking & Roadmap

### 🏁 Phase 1: Core Fundamentals (`01_beginner`)
Focuses on basic syntax patterns, flow control structures, input sanitization, error interception, and dynamic list arrays.

- [x] **Smart Calculator:** Basic operations, state processing, memory caching.
- [x] **Number Guessing Game:** Random state evaluation and adaptive delta feedback.
- [x] **Rock Paper Scissors:** Automated rule logic validation cycles.
- [x] **To-Do List:** Structural tasks, status mutations, and tracking configurations.
- [x] **Multi-Category Quiz Game:** Scaled across thematic dictionary profiles (Web Dev, Physics, Finance, Math) featuring copy-shuffling algorithms.

### ⛰️ Upcoming Milestones
- [ ] **Phase 2 (`02_beginner-intermediate`):** Local persistence engines (JSON structures / File system read-writes), custom module abstractions, and foundational decorators.
- [ ] **Phase 3 (`03_intermediate`):** Relational databases (`sqlite3` interaction layers), Object-Oriented Programming (OOP) structural enforcement, and multithreading basics.
- [ ] **Phase 5 (`05_ai-automation`):** API integration nodes, local cron automation, and lightweight web scraping frames.

---

## 🧠 Engineering Methodology

This codebase explicitly follows an iterative lifecycle workflow:
$$\text{Build} \longrightarrow \text{Refactor} \longrightarrow \text{Sanitize} \longrightarrow \text{Optimize} \longrightarrow \text{Repeat}$$

As application scopes scale out of the beginner directories, the repository will automatically inherit higher validation metrics, unit test definitions (`pytest`), configuration management layers (`.yaml`/`.env`), clean API interfaces, and persistent caching layers.

---

## 📄 License

This repository is distributed under the conditions of the open-source **MIT License**. Check the root `LICENSE` file template for contextual permissions.
