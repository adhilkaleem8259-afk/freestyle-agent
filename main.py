import asyncio
import logging
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# -------------------------------
# Agent imports
# -------------------------------
from agent.commands import CommandHandler
from agent.memory import MemoryManager
from agent.llm_agent import LLMHandler
from agent.loop_agent import LoopAgent
from agent.parallel_agent import ParallelAgent
from agent.sequential_agent import SequentialAgent
from agent.message_bus import MessageBus

# -------------------------------
# App initialization
# -------------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

# -------------------------------
# Memory, LLM, Commands
# -------------------------------
memory = MemoryManager("user_history.json")
llm = LLMHandler()
commands = CommandHandler(memory, llm)

# -------------------------------
# Logging with FileHandler + flush
# -------------------------------
logger = logging.getLogger("freestyle_agent")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# Custom FileHandler with flush
class FlushFileHandler(logging.FileHandler):
    def emit(self, record):
        super().emit(record)
        self.flush()

file_handler = FlushFileHandler("logs/agent.log", mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Make logging.getLogger() return this logger everywhere
logging.getLogger = lambda name=None: logger

# -------------------------------
# Message Bus
# -------------------------------
bus = MessageBus()

# -------------------------------
# Web Routes
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tasks")
async def get_tasks():
    return JSONResponse(content=commands.show_tasks())

@app.post("/add_task")
async def add_task(task: str = Form(...)):
    if task:
        commands.add_task(task)
        logger.info(f"[System] New task added: {task}")
    return JSONResponse({"status": "success"})

@app.get("/logs")
async def get_logs():
    try:
        with open("logs/agent.log", "r") as f:
            logs = f.read().splitlines()
    except FileNotFoundError:
        logs = []
    return JSONResponse({"logs": logs})

@app.post("/clear_logs")
async def clear_logs():
    open("logs/agent.log", "w").close()
    logger.info("[System] Logs cleared")
    return JSONResponse({"status": "success"})

# -------------------------------
# Agent orchestration
# -------------------------------
async def run_agents():
    loop_agent = LoopAgent("LoopAgent1", bus, commands)
    parallel_agent = ParallelAgent("ParallelAgent1", bus, commands)
    sequential_agent = SequentialAgent("SequentialAgent1", bus, commands)

    await asyncio.gather(
        loop_agent.run(),
        parallel_agent.run(),
        sequential_agent.run()
    )

# -------------------------------
# Startup event
# -------------------------------
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_agents())
