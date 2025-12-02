import sqlite3
import pandas as pd
import bcrypt

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

#C - CREATE     Insert new instances      
def add_user(conn, username, hashed_password, role = "user"):
    cursor = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) """) 
    param =  (username, hashed_password)
    cursor.execute(sql, param)
    conn.commit()

#R - READ   Reads the users from the table
def get_users(conn):
    cursor = conn.cursor()
    sql = ("""SELECT * FROM users""")
    cursor.execute(sql)
    users = cursor.fetchall()
    return users

def get_user(conn, name_):
    cursor = conn.cursor(conn, name_)
    sql = ("""SELECT * FROM users WHERE username == ?""")
    param = (name_,)
    cursor.execute(sql, param)
    user = cursor.fetchone()
    conn.close
    return user

# U - UPDATE       Modify existing data
def update_user_password(conn, username, new_password):
    cursor = conn.cursor()
    sql = ("""UPDATE users SET password_hash = ? WHERE username = ? """)
    param = (new_password, username)
    cursor.execute(sql, param)
    conn.commit()
    conn.close()

# D - DELETE    Remove data DELETE
def delete_user(conn, username):
    cursor = conn.cursor()
    sql = ("""DELETE FROM users WHERE username = ?""")
    param = (username)
    cursor.execute(sql, param)
    conn.commit()
    conn.close()

def user_login(conn):
    name = input("Enter your username to login: ")
    password = input("Enter your password to login: ")
    id, name_db, hash = get_user(conn, name)
    if name == name_db:
        return verify_password 