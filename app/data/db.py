import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("DATA") / "intelligence_platform.db"

def connect_database(conn):
    conn = sqlite3.connect('DATA/intelligence_platform.db', check_same_thread = False)
    return conn

def get_all_cyber_incidents(conn):
    sql = "SELECT * FROM cyber_incidents"
    data = pd.read_sql(sql, conn)
    return data