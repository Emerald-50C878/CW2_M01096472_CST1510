import bcrypt
import pandas as pd
import sqlite3
from app.data.users import get_user
from app.services.user_service import register_user, login_user
from pathlib import Path


def menu():
    print(" ---! Choose an option: !---")
    print("*=-[1] Register-=*")
    print("*=-[2] Login-=*")
    print("*=-[3] Exit-=*")

def main():
    while True:
        menu()
        try:
            choice = input("")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting safely...")
        returnchoice = input('')
        if choice == "1":
            register_user(username, password, role="user")
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

def create_user_table():
    cursor = conn.cursor()
    # Create table 
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL, role TEXT DEFAULT 'user' ) """)
    # Save changes 
    conn.commit()

def add_user(conn, username, hashed_password, role = "user"):
    cursor = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?) """) 
    param =  (username, hashed_password)
    cursor.execute(sql, param)
    conn.commit()

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
        username, hash = user.strip().split(",")
        print(user)
    return 

def select_user(cursor):
    cursor.execute("""SELECT * FROM users""") 
    all_users = cursor.fetchall() # Returns list of all rows

def migrate_cyber_table():
    cyber = pd.read_csv("DATA/cyber_incidents.csv")
    # View first 5 rows
    print(cyber.head()) # Check data types and missing values
    print(cyber.info()) # Check for missing data
    print(cyber.isnull().sum())
    # Connect to database
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    # Bulk insert all rows 
    cyber.to_sql( 'cyber_incidents', conn, if_exists='append', index=False ) 
    print("✓ Data loaded successfully")
    # Count rows in database 
    cursor = conn.cursor() 
    cursor.execute("SELECT COUNT(*) FROM cyber_incidents") 
    count = cursor.fetchone()[0] 
    print(f"Loaded {count} incidents") # View sample data cursor.execute("SELECT * FROM cyber_incidents LIMIT 3") 
    for row in cursor.fetchall(): 
        print(row)

def migrate_it_tickets():
    datait = pd.read_csv("DATA/it_tickets.csv")
    # View first 5 rows
    print(datait.head()) # Check data types and missing values
    print(datait.info()) # Check for missing data
    print(datait.isnull().sum())
    # Connect to database
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    # Bulk insert all rows 
    datait.to_sql( 'it_tickets', conn, if_exists='append', index=False ) 
    print("✓ Data loaded successfully")
