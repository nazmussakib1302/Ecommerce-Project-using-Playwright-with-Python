import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

USERNAME = os.getenv("DEMOBLAZE_USERNAME", "")
PASSWORD = os.getenv("DEMOBLAZE_PASSWORD", "")

TEST_DATA_DIR = ROOT_DIR / "test_data"
