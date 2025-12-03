import sqlite3
import pandas as pd


# ---- READ ----
def get_all_tickets(conn: sqlite3.Connection) -> pd.DataFrame:
    """Returns all IT ticket records from the database."""
    query = "SELECT * FROM it_tickets"
    return pd.read_sql_query(query, conn)


# ---- CREATE ----
def insert_ticket(conn: sqlite3.Connection, title: str, priority: str, status: str):
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO it_tickets (title, priority, status) VALUES (?, ?, ?)",
    (title, priority, status)
    )
    conn.commit()


# ---- UPDATE ----
def update_ticket(conn: sqlite3.Connection, ticket_id: int, title: str, priority: str, status: str):
    cur = conn.cursor()
    cur.execute(
    """
    UPDATE it_tickets
    SET title = ?, priority = ?, status = ?
    WHERE id = ?
    """,
    (title, priority, status, ticket_id)
    )
    conn.commit()


# ---- DELETE ----
def delete_ticket(conn: sqlite3.Connection, ticket_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM it_tickets WHERE id = ?", (ticket_id,))
    conn.commit()