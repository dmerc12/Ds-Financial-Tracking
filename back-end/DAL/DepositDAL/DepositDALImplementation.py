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
            deposit = Deposit(0, 0, 0, date(0000, 0, 0), '', 0.00)
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
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get all deposits with result: " +
                         str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def get_deposits_by_category(self, category_id: int) -> List[Deposit]:
        logging.info("Beginning DAL method get deposits by category with category ID: " + str(category_id))
        sql = "SELECT * from financial_tracker.Deposit WHERE category_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get all deposits by category with result: " +
                         str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def get_deposits_by_date(self, deposits_date: date) -> List[Deposit]:
        logging.info("Beginning DAL method get deposits by date with date: " + str(deposits_date))
        sql = "SELECT * from financial_tracker.Deposit WHERE date=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposits_date,))
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info(
                "Finishing DAL method get all deposits by date with result: " + str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def get_deposits_total_by_category(self, category_id: int) -> float:
        pass

    def get_deposits_total_by_month(self) -> float:
        pass

    def get_deposits_total_by_year(self) -> float:
        pass

    def get_deposits_by_description_key_words(self) -> List[Deposit]:
        pass

    def update_deposit(self, deposit: Deposit) -> Deposit:
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
        logging.info("Finishing DAL method update deposit with result: " + str(deposit.convert_to_dictionary()))
        return deposit

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
        pass
