#This file contains all of the migration algorithms and functions
import sqlite3
import pandas as pd


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
    cyber = cyber.read_csv("DATA/cyber_incidents.csv")
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