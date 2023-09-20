import sqlite3
import os

current_directory = os.getcwd()

database_path = os.path.join(current_directory, "Database.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE Category (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Expense (
        expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        description TEXT,
        amount FLOAT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Category(category_id)
    )
''')

cursor.execute('''
    CREATE TABLE Deposit (
        deposit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        description TEXT,
        amount FLOAT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Category(category_id)
    )
''')

connection.commit()
connection.close()

print("Database setup successfully!")
