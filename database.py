import sqlite3

# Connect to the database
conn = sqlite3.connect("expenses.db")

# Create cursor
cursor = conn.cursor()

# Create expenses table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL
)
""")

# Save changes
conn.commit()