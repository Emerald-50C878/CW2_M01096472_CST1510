import bcrypt
import pandas as pd
import sqlite3
from pathlib import Path
from login import login_user, register_user

def menu():
    print(" ---! Choose an option: !---")
    print("*=-[1] Register-=*")
    print("*=-[2] Login-=*")
    print("*=-[3] Exit-=*")

def main():
    while True:
        menu()
        choice = input('')
        if choice == "1":
            register_user()
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter Password: ")
            print(login_user(username, password))
        elif choice == '3':
            print("Good bye!") 
            break


if __name__ == "__main__":
    main()


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

def select_user(cursor):
    cursor.execute("""SELECT * FROM users""") 
    all_users = cursor.fetchall() # Returns list of all rows


cyber = pd.read_csv("DATA/cyber_incidents.csv")
print(cyber)

print(migrate_user_data)