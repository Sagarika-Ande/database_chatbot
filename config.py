import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ---------- DATABASE CONFIG ----------
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# ---------- LLM CONFIG ----------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
