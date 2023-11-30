import logging
from typing import List
from datetime import date

from DAL.DepositDAL.DepositDALInterface import DepositDALInterface
from Database.config import Connection
from Entities.Deposit import Deposit

class DepositDALImplementation(DepositDALInterface):

    def create_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning DAL method create deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "INSERT INTO financial_tracker.Deposit (user_id, category_id, date, description, amount) VALUES " \
              "(%s, %s, %s, %s , %s) RETURNING deposit_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit.user_id, deposit.category_id, deposit.date, deposit.description, deposit.amount))
        deposit.deposit_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create deposit with result: " + str(deposit.convert_to_dictionary()))
        return deposit

    def get_deposit(self, deposit_id: int) -> Deposit:
        logging.info("Beginning DAL method get deposit with deposit ID: " + str(deposit_id))
        sql = "SELECT * FROM financial_tracker.Deposit WHERE deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_id,))
        deposit_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if deposit_info is None:
            deposit = Deposit(0, 0, 0, date(1, 1, 1), '', 0.00)
            logging.info("Finishing DAL method get deposit, deposit not found")
            return deposit
        else:
            deposit = Deposit(*deposit_info)
            logging.info("Finishing DAL method get deposit with deposit: " + str(deposit.convert_to_dictionary()))
            return deposit

    def get_all_deposits(self, user_id: int) -> List[Deposit]:
        logging.info("Beginning DAL method get all deposits with user ID: " + str(user_id))
        sql = "SELECT * FROM financial_tracker.Deposit WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        deposit_records = cursor.fetchall()
        cursor.close()
        connection.close()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get all deposits with result: " +
                         str(deposit.convert_to_dictionary()))
        return deposits

    def get_deposits_by_category(self, category_id: int) -> List[Deposit]:
        logging.info("Beginning DAL method get deposits by category with category ID: " + str(category_id))
        sql = "SELECT * from financial_tracker.Deposit WHERE category_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        deposit_records = cursor.fetchall()
        cursor.close()
        connection.close()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get all deposits by category with result: " +
                         str(deposit.convert_to_dictionary()))
        return deposits

    def get_deposits_by_date(self, deposit_date: date) -> List[Deposit]:
        logging.info("Beginning DAL method get deposits by date with date: " + str(deposit_date))
        sql = "SELECT * from financial_tracker.Deposit WHERE EXTRACT(DAY FROM date)=%s " \
              "AND EXTRACT(MONTH FROM date)=%s AND EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_date.day, deposit_date.month, deposit_date.year))
        deposit_records = cursor.fetchall()
        cursor.close()
        connection.close()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info(
                "Finishing DAL method get all deposits by date with result: " + str(deposit.convert_to_dictionary()))
        return deposits

    def get_deposits_by_description_key_words(self, keywords: List[str]) -> List[Deposit]:
        logging.info("Beginning Deposit DAL method get deposits by description key words with keywords: " +
                     str(keyword for keyword in keywords))
        placeholders = ", ".join(['%s'] * len(keywords))
        sql = f"SELECT * FROM financial_tracker.Deposit WHERE description LIKE ANY(ARRAY[{placeholders}]);"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, tuple(f"%{keyword}%" for keyword in keywords))
        deposit_records = cursor.fetchall()
        cursor.close()
        connection.close()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get deposits by description keywords with result: " +
                         str(deposit.convert_to_dictionary()))
        return deposits

    def get_total_by_category(self, category_id: int) -> float:
        logging.info("Beginning Deposit DAL method get total by category with category ID: " + str(category_id))
        sql = "SELECT SUM(amount) FROM financial_tracker.Deposit WHERE category_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return total

    def get_total_by_month(self, month: int, year: int) -> float:
        logging.info("Beginning Deposit DAL method get total by category with category ID: " + str(month))
        sql = "SELECT SUM(amount) FROM financial_tracker.Deposit WHERE EXTRACT(MONTH FROM date)=%s AND " \
              "EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (month, year))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return total

    def get_total_by_year(self, year: int) -> float:
        logging.info("Beginning Deposit DAL method get total by category with category ID: " + str(year))
        sql = "SELECT SUM(amount) FROM financial_tracker.Deposit WHERE EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (year,))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return total

    def update_deposit(self, deposit: Deposit) -> bool:
        logging.info("Beginning DAL method update deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.Deposit SET category_id=%s, date=%s, description=%s, amount=%s WHERE " \
              "deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit.category_id, deposit.date, deposit.description, deposit.amount,
                             deposit.deposit_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update deposit")
        return True

    def delete_deposit(self, deposit_id: int) -> bool:
        logging.info("Beginning DAL method delete deposit with deposit ID: " + str(deposit_id))
        sql = "DELETE FROM financial_tracker.Deposit WHERE deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete deposit")
        return True

    def delete_all_deposits(self, user_id: int) -> bool:
        logging.info("Beginning DAL method delete all deposits with user ID: " + str(user_id))
        sql = "DELETE FROM financial_tracker.Deposit WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete all deposits")
        return True
