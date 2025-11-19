import sqlite3
import pandas as pd

#create user table
def create_user_table(conn):
    cursor = conn.cursor()
    # Create table 
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, role TEXT DEFAULT 'user' ) """)
    # Save changes 
    conn.commit()