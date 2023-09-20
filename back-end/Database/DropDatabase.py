import sqlite3
import os

database_path = os.path.join(os.getcwd(), "Database.db")

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS Expense
""")

cursor.execute("""
    DROP TABLE IF EXISTS Deposit
""")

cursor.execute("""
    DROP TABLE IF EXISTS Category
""")

connection.commit()
connection.close()

print("Database teardown completed successfully!")
