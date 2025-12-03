import sqlite3
import pandas as pd

# ---- CREATE ----
def insert_dataset(conn: sqlite3.Connection, name: str, description: str, source: str):
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO datasets_metadata (name, description, source) VALUES (?, ?, ?)",
    (name, description, source)
    )
    conn.commit()
    return cur.lastrowid


# ---- READ ----
def get_all_datasets(conn: sqlite3.Connection) -> pd.DataFrame:
    """Returns all dataset metadata records from the database."""
    query = "SELECT * FROM datasets_metadata"
    return pd.read_sql_query(query, conn, __name__)


# ---- UPDATE ----
def update_dataset(conn: sqlite3.Connection, dataset_id: int, name: str, description: str, source: str):
    cur = conn.cursor()
    cur.execute(
    """
    UPDATE datasets_metadata
    SET name = ?, description = ?, source = ?
    WHERE id = ?
    """,
    (name, description, source, dataset_id)
    )
    conn.commit()

# ---- DELETE ----
def delete_dataset(conn: sqlite3.Connection, dataset_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM datasets_metadata WHERE id = ?", (dataset_id,))
    conn.commit()
    return cur.rowcount