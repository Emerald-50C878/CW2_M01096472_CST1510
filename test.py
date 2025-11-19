import pandas as pd
import sqlite3

#connect to database 
conn = sqlite3.connect("DATA/intelligence_platform.db")

def add_user(conn, name, hash):
    cursor = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) """) 
    param =  (sql, hash)
    cursor.execute(sql,param)
    conn.commit()

def get_users():
    cursor = conn.cursor()
    sql = ("""SELECT * FROM users""")
    cursor.execute(sql)
    users = cursor.fetchall()
    conn.close()
    return users

def migrate_user_data():
    with open("DATA/users.txt", "r") as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(",")
        print(user)
    conn.close()

