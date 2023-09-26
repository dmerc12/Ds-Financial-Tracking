import logging
from typing import List

from DAL.DepositDAL.DepositDALInterface import DepositDALInterface
from Database.config import Connection
from Entities.Deposit import Deposit

class DepositDALImplementation(DepositDALInterface):

    def create_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning DAL method create deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "INSERT INTO Deposit (category_id, date, description, amount)VALUES(?, ?, ? , ?) RETURNING deposit_id"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit.category_id, deposit.date, deposit.description, deposit.amount))
        deposit.deposit_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create deposit with result: " + str(deposit.convert_to_dictionary()))
        return deposit

    def get_all_deposits(self) -> List[Deposit]:
        logging.info("Beginning DAL method get all deposits")
        sql = "SELECT * FROM Deposit"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(*deposit)
            deposits.append(deposit)
            logging.info("Finishing DAL method get all categories with result: " + str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.commit()
        connection.close()
        return deposits

    def update_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning DAL method update deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "UPDATE Deposit SET category_id=?, date=?, description=?, amount=? WHERE deposit_id=?"
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
        sql = "DELETE FROM Deposit WHERE deposit_id=?"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete deposit")
        return True
