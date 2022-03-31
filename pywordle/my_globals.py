"""
App globals
"""

from pathlib import Path

from pywordle.logic.helper import get_app_major_version

WORKING_DIR = Path(__file__).absolute().parent.parent
DATABASE_FILE = f"db_v{get_app_major_version(WORKING_DIR)}.X.sqlite3"
DATABASE_URL = f"sqlite:///{WORKING_DIR}/{DATABASE_FILE}"
