import pandas as pd
import sqlite3

#connect to database
conn = sqlite3.connect("DATA/intelligence_platform.db")

def create_user_table():
    cursor = conn.cursor()
    # Create table 
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, role TEXT DEFAULT 'user' ) """)
    # Save changes 
    conn.commit()

def add_user(conn, name, hash):
    cursor = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) """) 
    param =  (name, hash)
    cursor.execute(sql, param)
    conn.commit()
    conn.close()

def get_users():
    cursor = conn.cursor()
    sql = ("""SELECT * FROM users""")
    cursor.execute(sql)
    users = cursor.fetchall()
    return users

def migrate_user_data():
    with open("DATA/users.txt", "r") as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(",")
        print(user)

