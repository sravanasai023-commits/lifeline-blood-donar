-- Create Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Create Donors Table
CREATE TABLE donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL,
    blood_group TEXT NOT NULL,
    city TEXT NOT NULL,
    address TEXT NOT NULL,
    last_donation TEXT,
    availability TEXT NOT NULL
);

-- Create Blood Requests Table
CREATE TABLE blood_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    hospital TEXT NOT NULL,
    city TEXT NOT NULL,
    phone TEXT NOT NULL,
    required_date TEXT NOT NULL,
    notes TEXT
);

-- Create Contacts Table
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
);