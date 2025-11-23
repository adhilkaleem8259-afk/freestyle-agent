import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_HISTORY_FILE = os.path.join(BASE_DIR, "data", "user_history.json")
