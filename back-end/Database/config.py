import os

import mysql.connector


class Connection:
    @staticmethod
    def db_connection():
        try:
            new_connection = mysql.connector.connect(
                host=os.environ.get("HOST"),
                dbname=os.environ.get("DBNAME"),
                user=os.environ.get("USER"),
                password=os.environ.get("PASSWORD"),
                port=os.environ.get("PORT")
            )
            return new_connection
        except mysql.connector.Error:
            raise mysql.connector.Error("Could not connect to the database, please try again!")

connection = Connection.db_connection()
print("Connected to the database successfully!")
