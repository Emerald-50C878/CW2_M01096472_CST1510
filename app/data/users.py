import sqlite3
import pandas as pd
import bcrypt

def select_user(cursor):
    cursor.execute("""SELECT * FROM users""") 
    all_users = cursor.fetchall() # Returns list of all rows


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt=bcrypt.gensalt())
    return hashed.decode('utf-8')

def is_valid_hash(password: str, hashed_password: str) -> bool:
    """
    Validates a plain-text password against a stored bcrypt hash.
    
    Args:
        password: The plain-text password provided by the user.
        hashed_password: The hash retrieved from the database (must be a string).
        
    Returns:
        True if the password matches the hash, False otherwise.
    """
    try:
        # We encode both the plain password and the stored hash (which is a string) 
        # back to bytes for bcrypt.checkpw
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        print(f"Error validating hash: {e}")
        return False

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
    cursor = conn.cursor()
    sql = ("""SELECT * FROM users WHERE username == ?""")
    param = (name_,)
    cursor.execute(sql, param)
    user = cursor.fetchone()
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
    verify_password = bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
    if name == name_db:
        return verify_password 