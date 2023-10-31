from typing import List

from DAL.DepositDAL.DepositDALInterface import DepositDALInterface
from Database.config import Connection
from Entities.Deposit import Deposit
from run import app


class DepositDALImplementation(DepositDALInterface):

    def create_deposit(self, deposit: Deposit) -> Deposit:
        app.logging.info("Beginning DAL method create deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "INSERT INTO financial_tracker.Deposit (category_id, date, description, amount) VALUES " \
              "(%s, %s, %s , %s) RETURNING deposit_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit.category_id, deposit.date, deposit.description, deposit.amount))
        deposit.deposit_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        app.logging.info("Finishing DAL method create deposit with result: " + str(deposit.convert_to_dictionary()))
        return deposit

    def get_deposit(self, deposit_id: int) -> Deposit:
        app.logging.info("Beginning DAL method get deposit with deposit ID: " + str(deposit_id))
        sql = "SELECT * FROM financial_tracker.Deposit WHERE deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_id,))
        deposit_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if deposit_info is None:
            deposit = Deposit(0, 0, '', '', 0.00)
            app.logging.info("Finishing DAL method get deposit, deposit not found")
            return deposit
        else:
            deposit = Deposit(*deposit_info)
            app.logging.info("Finishing DAL method get deposit with deposit: " + str(deposit.convert_to_dictionary()))
            return deposit

    def get_all_deposits(self) -> List[Deposit]:
        app.logging.info("Beginning DAL method get all deposits")
        sql = "SELECT * FROM financial_tracker.Deposit;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(
                deposit_id=deposit[0],
                category_id=deposit[4],
                date=deposit[1],
                description=deposit[2],
                amount=deposit[3]
            )
            deposits.append(deposit)
            app.logging.info("Finishing DAL method get all deposits with result: " +
                             str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def get_deposits_by_category(self, category_id: int) -> List[Deposit]:
        app.logging.info("Beginning DAL method get deposits by category with category ID: " + str(category_id))
        sql = "SELECT * from financial_tracker.Deposit WHERE category_id=?;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(
                deposit_id=deposit[0],
                category_id=deposit[4],
                date=deposit[1],
                description=deposit[2],
                amount=deposit[3]
            )
            deposits.append(deposit)
            app.logging.info("Finishing DAL method get all deposits by category with result: " +
                             str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def get_deposits_by_date(self, date: str) -> List[Deposit]:
        app.logging.info("Beginning DAL method get deposits by date with date: " + str(date))
        sql = "SELECT * from financial_tracker.Deposit WHERE date=?;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        deposit_records = cursor.fetchall()
        deposits = []
        for deposit in deposit_records:
            deposit = Deposit(
                deposit_id=deposit[0],
                category_id=deposit[4],
                date=deposit[1],
                description=deposit[2],
                amount=deposit[3]
            )
            deposits.append(deposit)
            app.logging.info(
                "Finishing DAL method get all deposits by date with result: " + str(deposit.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return deposits

    def update_deposit(self, deposit: Deposit) -> Deposit:
        app.logging.info("Beginning DAL method update deposit with data: " + str(deposit.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.Deposit SET category_id=%s, date=%s, description=%s, amount=%s WHERE " \
              "deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit.category_id, deposit.date, deposit.description, deposit.amount,
                             deposit.deposit_id))
        cursor.close()
        connection.commit()
        connection.close()
        app.logging.info("Finishing DAL method update deposit with result: " + str(deposit.convert_to_dictionary()))
        return deposit

    def delete_deposit(self, deposit_id: int) -> bool:
        app.logging.info("Beginning DAL method delete deposit with deposit ID: " + str(deposit_id))
        sql = "DELETE FROM financial_tracker.Deposit WHERE deposit_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_id,))
        cursor.close()
        connection.commit()
        connection.close()
        app.logging.info("Finishing DAL method delete deposit")
        return True
