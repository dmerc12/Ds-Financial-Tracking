import sqlite3


class Connection:
    @staticmethod
    def db_connection():
        try:
            new_connection = sqlite3.connect('/Users/dylanmercer12/Desktop/Projects/FinancialTrackingApp/back-end/'
                                             'Database/Database.db')
            return new_connection
        except sqlite3.Error:
            raise sqlite3.Error("Could not connect to the database, please try again!")

connection = Connection.db_connection()
print("Connected to the database successfully!")
