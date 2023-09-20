import sqlite3
import os

class Connection:
    @staticmethod
    def db_connection():
        try:
            database_path = os.path.join(os.getcwd(), "Database.db")

            new_connection = sqlite3.connect(database_path)
            return new_connection
        except sqlite3.Error as error:
            raise sqlite3.Error("Could not connect to the database, please try again!")

connection = Connection.db_connection()
print(connection)
