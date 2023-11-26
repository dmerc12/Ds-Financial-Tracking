import logging

from DAL.UserDAL.UserDALInterface import UserDALInterface
from Database.config import Connection
from Entities.User import User


class UserDALImplementation(UserDALInterface):

    def create_user(self, user: User) -> User:
        logging.info("Beginning DAL method create user with user: " + str(user.convert_to_dictionary()))
        sql = "INSERT INTO financial_tracker.User (email, passwrd) VALUES (%s, %s) RETURNING user_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.email, user.password))
        connection.commit()
        user_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        user.user_id = user_id
        logging.info("Finishing DAL method create user")
        return user

    def get_user_by_id(self, user_id: int) -> User:
        logging.info("Beginning DAL method get user by ID with ID: " + str(user_id))
        sql = "SELECT * FROM financial_tracker.User WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, '', '')
            logging.info("Finishing DAL method get user by ID, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method get user by ID with user: " + str(user.convert_to_dictionary()))
            return user

    def get_user_by_email(self, email: str) -> User:
        logging.info("Beginning DAL method get user by email with email: " + str(email))
        sql = "SELECT * FROM financial_tracker.User WHERE email=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, '', '')
            logging.info("Finishing DAL method get user by email, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method get user by email with user: " + str(user.convert_to_dictionary()))
            return user

    def login(self, email: str, password: str) -> User:
        logging.info("Beginning DAL method login with email: " + str(email) + " and password: " + str(password))
        sql = "SELECT * FROM financial_tracker.User WHERE email=%s and passwrd=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (email, password))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, '', '')
            logging.info("Finishing DAL method login, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method login with user: " + str(user.convert_to_dictionary()))
            return user

    def change_email(self, user: User) -> bool:
        logging.info("Beginning DAL method update user with user: " + str(user.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.User SET email=%s WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.email, user.user_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method change email")
        return True

    def change_password(self, user: User) -> bool:
        logging.info("Beginning DAL method change password with user: " + str(user.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.User SET passwrd=%s WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.password, user.user_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method change password")
        return True

    def delete_user(self, user_id) -> bool:
        logging.info("Beginning DAL method delete user with user ID: " + str(user_id))
        sql = "DELETE FROM financial_tracker.User WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete user")
        return True
