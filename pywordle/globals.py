from pathlib import Path

from pywordle.logic.helper import get_app_major_version

WORKING_DIR = Path(__file__).parent.parent
DATABASE_FILE = f"db_v{get_app_major_version()}.X.sqlite3"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
