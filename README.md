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
- log will update every 2 seconds

4. Offline & Lightweight
No external APIs needed.  
Runs on any machine with Python installed.


🛠️ Tech Stack

Languages:

- Python
- JavaScript
- HTML
- CSS

Frameworks & Libraries:

- FastAPI – Backend web framework for building APIs
- Uvicorn – ASGI server to run FastAPI
- Jinja2 – Template engine for HTML rendering
- Rich – Advanced terminal UI (colored output, tables, panels)
- python-dotenv – Environment variable management (.env loading)

Tools:

- Python 3.x – Main programming language
- Git & GitHub – Version control and repository hosting
- VS Code – Development editor
- Environment Variables (.env) – Secure configuration handling




🧠 How the System Works

main.py
- Displays Rich UI header  
- Loads user history  
- Prompts user for input  
- Sends requests to orchestrator  
- Displays formatted responses  

orchestrator.py
This is the “brain”:
- Defines multiple agents  
- Chooses correct agent based on user input  
- Returns structured results  

You can easily add more agents like:
```python
def new_agent(task):
    return "Result of new agent"
```
Then register it inside the orchestrator.





📁 Project Structure


freestyle_agent/
|
│   main.py
│   orchestrator.py
│   requirements.txt
│   user_history.json
│
├───agent/
│   │   commands.py
│   │   llm_agent.py
│   │   loop_agent.py
│   │   memory.py
│   │   message_bus.py
│   │   parallel_agent.py
│   │   sequential_agent.py
│   │   __init__.py
|
├───data/
│       user_history.json
│
├───logs/
│       agent.log
│
├───tools/
│   │   toolbox.py
│   │   __init__.py
│
├───ui/
│   │   terminal_ui.py
│   │   __init__.py
│   
├───utils/
│   │   config.py
│   │   helpers.py
│   │   __init__.py
│
└───web/
    │   __init__.py
    │
    ├───static/
    │       script.js
    │       style.css
    │
    └───templates/
            index.html
            log_panel.html


⚙️ Installation
1. Clone the repository
   
git clone https://github.com/username/repository.git
cd repository

2. Create virtual environment (optional but recommended)
   
python -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows

3. Install dependencies
   
pip install -r requirements.txt




▶️ Run the Project
Example (FastAPI):
//run this code
uvicorn main:app --reload


Or if Python script:
//run this code
python main.py

To stop the server:
ctrl + c

📘 Usage

<img width="1920" height="1080" alt="Screenshot 2025-11-25 150233" src="https://github.com/user-attachments/assets/6d0e52ab-579b-4996-8a26-1a2f19b02aa3" />
<img width="1920" height="1080" alt="Screenshot 2025-11-25 150212" src="https://github.com/user-attachments/assets/90c3907b-e617-46ed-9e1f-83ea2c398812" />
<img width="1920" height="1080" alt="Screenshot 2025-11-25 150328" src="https://github.com/user-attachments/assets/8cdae0b3-aaff-4b01-a28a-73104dae279a" />
<img width="1920" height="1080" alt="Screenshot 2025-11-25 150302" src="https://github.com/user-attachments/assets/f4113a06-cbed-4236-b87a-a7a393f6cf5e" />
<img width="1920" height="1080" alt="Screenshot 2025-11-25 150242" src="https://github.com/user-attachments/assets/f738d508-eb46-490c-8aea-e5d1d378ac76" />


🛠️ Future Enhancements
These will make the project even stronger:
- Parallel execution agents  
- File analyzing agent  
- Conversational memory expansion  
- Web dashboard using FastAPI  
- Integration with local ML models  


👤 Author
Adhilmohamed Kaleem
Freestyle Agent Developer  
Built as part of coding


📜 License
Open for educational and personal use.

