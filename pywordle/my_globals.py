"""
App globals
"""

from pathlib import Path

WORKING_DIR = Path(__file__).absolute().parent.parent
DATABASE_FILE = "db.sqlite3"
DATABASE_URL = f"sqlite:///{WORKING_DIR}/{DATABASE_FILE}"
