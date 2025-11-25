Freestyle Agent

Freestyle Agent is a modular, offline‑capable AI task assistant built in Python.  
It provides an extendable multi‑agent architecture, a Rich‑powered CLI interface, and an automatic user history system.

📌 Overview
Freestyle Agent is designed as a flexible offline assistant that can:
- Run multiple agent functions inside a single orchestrator  
- Remember user preferences through history  
- Provide a clean interactive terminal UI using **Rich**  
- Allow extension into multi‑agent or parallel‑agent systems  

This project is part of a hands‑on practical build for automation, AI usability, and offline agent experimentation.




🚀 Features

1. Modular Agent Architecture
The core of the project lies in `orchestrator.py`, which:
- Routes tasks to the correct agent
- Supports adding unlimited new agents
- Makes the system scalable and extendable

2. Interactive CLI (Rich UI)
The main interface (`main.py`) uses **Rich**:
- Colorful panels  
- Tables  
- Styled prompts  
- A clean, readable command‑line experience  

3. Persistent User History
The file `user_history.json` automatically:
- Saves past user data  
- Loads previous sessions  
- Allows personalization for responses  

4. Offline & Lightweight
No external APIs needed.  
Runs on any machine with Python installed.


🛠️ Tech Stack

Languages:

Python / JavaScript / HTML / CSS.

Frameworks & Libraries:

FastAPI / React / Node / TensorFlow / etc.

Tools:

Docker / Git / VSCode / etc.
