import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    logging.basicConfig(
        filename=os.path.join(LOG_DIR, "agent.log"),
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    logging.info("=== Freestyle Agent Started ===")

def format_task(task):
    return task.strip().title()
