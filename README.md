**Freestyle Agent**

Freestyle Agent is a modular, offline‑capable AI task assistant built in Python.  
It provides an extendable multi‑agent architecture, a Rich‑powered CLI interface, and an automatic user history system.

**📌 Overview**
Freestyle Agent is designed as a flexible offline assistant that can:
- Run multiple agent functions inside a single orchestrator  
- Remember user preferences through history  
- Provide a clean interactive terminal UI using **Rich**  
- Allow extension into multi‑agent or parallel‑agent systems  

This project is part of a hands‑on practical build for automation, AI usability, and offline agent experimentation.




**🚀 Features**

**1. Modular Agent Architecture**
The core of the project lies in `orchestrator.py`, which:
- Routes tasks to the correct agent
- Supports adding unlimited new agents
- Makes the system scalable and extendable

**2. Interactive CLI (Rich UI)**
The main interface (`main.py`) uses **Rich**:
- Colorful panels  
- Tables  
- Styled prompts  
- A clean, readable command‑line experience  

**3. Persistent User History**
The file `user_history.json` automatically:
- Saves past user data  
- Loads previous sessions  
- Allows personalization for responses
- log will update every 2 seconds

**4. Offline & Lightweight**
No external APIs needed.  
Runs on any machine with Python installed.


**🛠️ Tech Stack**

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




**🧠 How the System Works**

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





**📁 Project Structure**


<img width="284" height="883" alt="6" src="https://github.com/user-attachments/assets/6de0fa9d-2166-46dd-a658-8f1e97af1639" />




**⚙️ Installation**
1. Clone the repository
   
git clone https://github.com/adhilkaleem8259-afk/freestyle-agent.git
cd repository

2. Create virtual environment (optional but recommended)
   
python -m venv venv
source venv/bin/activate       # Mac / Linux
venv\Scripts\activate          # Windows

3. Install dependencies
   
pip install -r requirements.txt




**▶️ Run the Project**
Example (FastAPI):
//run this code
uvicorn main:app --reload


Or if Python script:
//run this code
python main.py

To stop the server:
ctrl + c


**📘 Usage**

<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/f6c0ba37-6f34-4fe2-95a9-48b312c13cb7" />
<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/b421c755-8958-4815-a75b-a56afd489262" />
<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/400528b7-3d61-419f-806d-a776b9b46868" />
<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/5e7e9187-e32c-4b75-9b00-f26ed6353870" />
<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/0ee1bfa8-a462-433e-bbed-f846527d30f2" />




**🛠️ Future Enhancements**
These will make the project even stronger:
- Parallel execution agents  
- File analyzing agent  
- Conversational memory expansion  
- Web dashboard using FastAPI  
- Integration with local ML models  


**👤 Author**

**Adhilmohamed Kaleem**

Freestyle Agent Developer  
Built as part of coding


**📜 License**

Open for educational and personal use.

