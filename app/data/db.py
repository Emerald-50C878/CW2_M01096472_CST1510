import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("DATA") / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    """Connect to SQLite database."""
    return sqlite3.connect(str(db_path))

def get_all_cyber_incidents(conn, DATA_PATH):
    sql = "SELECT * FROM cyber_incidents"
    data = pd.read_sql(sql, conn)
    return data