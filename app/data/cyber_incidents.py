import pandas as pd
import sqlite3
from db import connect_database
import os

def migrate_users_from_file(conn, filepath="users.txt"):
    if not os.path.exists(filepath):
        print(f"⚠ File not found: {filepath}")
        print("No users to migrate.")
        return

    cursor = conn.cursor()
    migrated_count = 0

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Parse line: username,password_hash
            parts = line.split(',')
            if len(parts) >= 2:
                username = parts[0]
                password_hash = parts[1]

                # Insert user (ignore if already exists)
                try:
                    cursor.execute(
                        "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                        (username, password_hash, 'user')
                    )
                    if cursor.rowcount > 0:
                        migrated_count += 1
                except sqlite3.Error as e:
                    print(f"Error migrating user {username}: {e}")

    conn.commit()
    print(f"✅ Migrated {migrated_count} users from {filepath_name.name}")

def migrate_cyber_incidents(conn):
    path = "DATA/cyber_incidents.csv"
    df = pd.read.csv(path)
    print(df.head())
    df.to_sql('cyber_incidents', conn, if_exists = 'append', index = False)
    print("Data loaded successfully! ")

def get_all_cyber_incidents(conn):
    sql = "SELECT * FROM cyber_incidents"
    data = pd.read_sql(sql, conn)
    return data

def create_cyber_incidents_table(conn):
    """
    Create the cyber_incidents table.
    """
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            incident_type TEXT,
            severity TEXT,
            status TEXT,
            description TEXT,
            reported_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    print("✓ cyber_incidents table ready.")


def create_datasets_metadata_table(conn):
    """
    Create the datasets_metadata table.
    """
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT NOT NULL,
            category TEXT,
            source TEXT,
            last_updated TEXT,
            record_count INTEGER,
            file_size_mb REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    print("✓ datasets_metadata table ready.")


def create_it_tickets_table(conn):
    """
    Create the it_tickets table.
    """
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            priority TEXT,
            status TEXT,
            category TEXT,
            subject TEXT NOT NULL,
            description TEXT,
            created_date TEXT,
            resolved_date TEXT,
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    print("✓ it_tickets table ready.")
def create_all_tables(conn):
    """Create all necessary tables in the database."""
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)


conn = connect_database("DATA/intelligence_platform.db")
create_all_tables(conn)
print("✓ All tables created successfully.")
migrate_users_from_file(conn, filepath = "DATA/users.txt")
migrate_cyber_incidents(conn)