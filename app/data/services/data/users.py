import sqlite3
import pandas as pd

def add_user(conn, username, hashed_password, role = "user"):
    cursor = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) """) 
    param =  (username, hashed_password)
    cursor.execute(sql, param)
    conn.commit()

def get_users(conn):
    cursor = conn.cursor()
    sql = ("""SELECT * FROM users""")
    cursor.execute(sql)
    users = cursor.fetchall()
    return users