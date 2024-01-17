import os

from psycopg import connect, OperationalError


class Connection:
    @staticmethod
    def db_connection():
        try:
            new_connection = connect(
                host=os.environ.get("HOST"),
                dbname=os.environ.get("DBNAME"),
                user=os.environ.get("USER"),
                password=os.environ.get("PASSWORD"),
                port=os.environ.get("PORT")
            )
            return new_connection
        except OperationalError:
            raise OperationalError("Could not connect to the database, please try again!")

connection = Connection.db_connection()
print("Connected to the database successfully!")
