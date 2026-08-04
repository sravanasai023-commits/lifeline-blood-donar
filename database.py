import sqlite3

conn = sqlite3.connect("lifelink.db")
cur = conn.cursor()

# Users Table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    blood_group TEXT,
    city TEXT
)
""")

# Donors Table
cur.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    gender TEXT,
    age INTEGER,
    blood_group TEXT,
    city TEXT,
    address TEXT,
    last_donation TEXT,
    availability TEXT
)
""")

# Blood Requests Table
cur.execute("""
CREATE TABLE IF NOT EXISTS blood_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    blood_group TEXT,
    hospital TEXT,
    city TEXT,
    phone TEXT,
    required_date TEXT,
    notes TEXT
)
""")

# Contact Table
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully ✅")