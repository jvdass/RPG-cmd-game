# ⚔️ RPG-cmd-game

A minimalist, text-based RPG built with **Python**, focusing on a strategic elemental combat system, interactive gameplay loops, and clean terminal output.

---

## ✨ Overview
This project is a terminal-based role-playing game that uses a classic elemental system. It was designed with a focus on clean code structure, Object-Oriented Programming (OOP), and a minimalist user experience inspired by modern productivity tools.

## 🕹️ Core Features
* **Interactive Main Menu:** A polished entry layout offering options to launch a **New Game**, consult the comprehensive **Game Manual**, or safely **Exit**.
* **Elemental Triad**: Strategic turn-based combat based on strict strengths and weaknesses (🔥 Fire > 🌿 Plant > 💧 Water > 🔥 Fire).
* **In-Game Economy & Shop System:** A dynamic shop (`shop.py`) allowing players to spend gold earned from battles to purchase consumables (Health Potions) or permanently equip upgraded gear (Steel Sword, Heavy Armor) that instantly scales player statistics.
* **Visual UX Enhancements:** Built using custom terminal styling (`Style` configurations via ANSI escape codes) to deliver a colored, readable, and engaging interface directly inside the console.

## 🛠️ Technical Stack & Concepts
* **Language**: Python 3.x
* **Object-Oriented Programming (OOP):** Encapsulating state behavior inside cleanly defined Python classes (Player, Enemy).
* **Data Structures & Manipulation:** Handling nested dictionaries, mutating object properties safely, and validating key indices without data-type mismatches.
* **Source Control Management:** Structuring professional version tracking workflows using Git and GitHub.

---

## 📂 Project Architecture

The project is structured modularly to isolate concerns and enforce clean code practices:

```text
RPG-cmd-game/
│
├── main.py          # Application entry point & Main Menu loop
├── shop.py          # Shop management logic and transaction flows
├── entities.py      # Core classes (Player, Enemy, Style configuration)
└── README.md        # Project documentation
```

## 🚀 Quick Start
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/jvdass/RPG-cmd-game.git](https://github.com/jvdass/RPG-cmd-game.git)
