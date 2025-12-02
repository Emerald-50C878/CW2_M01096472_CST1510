import sqlite3
import pandas as pd

#create user table
def create_user_table(conn):
    cursor = conn.cursor()
    # Create table 
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, role TEXT DEFAULT 'user' ) """)
    # Save changes 
    conn.commit()

def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)