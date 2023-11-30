import logging
from typing import List
from datetime import date

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALInterface import DepositSALInterface
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.Deposit import Deposit


class DepositSALImplementation(DepositSALInterface):
    category_dao = CategoryDALImplementation()
    category_sao = CategorySALImplementation(category_dao)
    user_dao = UserDALImplementation()
    user_sao = UserSALImplementation(user_dao)

    def __init__(self, deposit_dao: DepositDALImplementation):
        self.deposit_dao = deposit_dao

    def create_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning SAL method create deposit with data: " + str(deposit.convert_to_dictionary()))
        if type(deposit.category_id) is not int:
            logging.warning("Error in SAL method create deposit, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif type(deposit.user_id) is not int:
            logging.warning("Error in SAL method create deposit, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif deposit.category_id == 0:
            logging.warning("Error in SAL method create deposit, category ID not set")
            raise CustomError("A category must be set, please try again!")
        elif not isinstance(deposit.date, date):
            logging.warning("Error in SAL method create deposit, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif deposit.date == date(1, 1, 1):
            logging.warning("Error in SAL method create deposit, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(deposit.description) is not str:
            logging.warning("Error in SAL method create deposit, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif deposit.description == "":
            logging.warning("Error in SAL method create deposit, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif deposit.amount <= 0.00:
            logging.warning("Error in SAL method create deposit, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.user_sao.get_user_by_id(deposit.user_id)
            self.category_sao.get_category(deposit.category_id)
            result = self.deposit_dao.create_deposit(deposit)
            logging.info("Finishing SAL method create deposit with result: " + str(deposit.convert_to_dictionary()))
            return result

    def get_deposit(self, deposit_id: int) -> Deposit:
        logging.info("Beginning SAL method get deposit with deposit ID: " + str(deposit_id))
        if type(deposit_id) is not int:
            logging.warning("Error in SAL method get deposit, deposit ID not an integer")
            raise CustomError("The deposit ID field must be an integer, please try again!")
        else:
            deposit = self.deposit_dao.get_deposit(deposit_id)
            if deposit.deposit_id == 0 and deposit.category_id == 0 and deposit.date == \
                    date(1, 1, 1) and deposit.description == "" and deposit.amount == 0.00:
                logging.warning("Error in SAL method get deposit, deposit not found")
                raise CustomError("Deposit not found, please try again!")
            else:
                logging.info("Finishing SAL method get deposit with result: " + str(deposit.convert_to_dictionary()))
                return deposit

    def get_all_deposits(self, user_id: int) -> List[Deposit]:
        logging.info("Beginning SAL method get all deposits")
        deposits = self.deposit_dao.get_all_deposits(user_id)
        if len(deposits) == 0:
            logging.warning("Error in SAL method get all categories, none found")
            raise CustomError("No deposits found, please try again!")
        else:
            logging.info("Finishing SAL method get all deposits")
            return deposits

    def get_deposits_by_category(self, category_id: int) -> List[Deposit]:
        logging.info("Beginning SAL method get deposits by category with category ID: " + str(category_id))
        if type(category_id) is not int:
            logging.warning("Error in SAL method get deposits by category, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        else:
            self.category_sao.get_category(category_id)
            deposits = self.deposit_dao.get_deposits_by_category(category_id)
            if len(deposits) == 0:
                logging.warning("Error in SAL method get deposits by category, none found")
                raise CustomError("No deposits found, please try again!")
            else:
                logging.info("Finishing SAL method get deposits by category")
                return deposits

    def get_deposits_by_date(self, deposit_date: date) -> List[Deposit]:
        logging.info("Beginning SAL method get deposits by date with date: " + str(deposit_date))
        if not isinstance(deposit_date, date):
            logging.warning("Error in SAL method get deposits by date, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif deposit_date == date(1, 1, 1):
            logging.warning("Error in SAL method get deposits by date, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        else:
            deposits = self.deposit_dao.get_deposits_by_date(deposit_date)
            if len(deposits) == 0:
                logging.warning("Error in SAL method get deposits by date, none found")
                raise CustomError("No deposits found, please try again!")
            else:
                logging.info("Finishing SAL method get deposits by date")
                return deposits

    def get_deposits_by_description_key_words(self, keywords: List[str]) -> List[Deposit]:
        logging.info("Beginning SAL method get deposits by description key words with keywords: " + str(keywords))
        for keyword in keywords:
            if type(keyword) is not str:
                logging.warning("Error in SAL method get deposits by description key words, keyword not a string")
                raise CustomError("The key words must be strings, please try again!")
        deposits = self.deposit_dao.get_deposits_by_description_key_words(keywords)
        if len(deposits) == 0:
            logging.warning("Error in SAL method get deposits by description key words, no deposits found")
            raise CustomError("No deposits found, please try again!")
        else:
            logging.info("Finishing SAL method get deposits by description key words")
            return deposits

    def get_total_by_category(self, category_id: int) -> float:
        logging.info("Beginning Deposit SAL method get total by category with category ID: " + str(category_id))
        if type(category_id) is not int:
            logging.warning("Error in Deposit SAL method get total by category, category ID not an integer")
            raise CustomError("The category ID field must be an integer please try again")
        else:
            category = self.category_sao.get_category(category_id)
            deposits = self.get_all_deposits(category.user_id)
            total = 0.00
            for deposit in deposits:
                if deposit.category_id == category_id:
                    total = total + deposit.amount
            if total == 0.00 or total == 0:
                logging.warning("Error in Deposit SAL method get total by category, no deposits with this category")
                raise CustomError("No deposits found, please try again!")
            else:
                total = self.deposit_dao.get_total_by_category(category_id)
                logging.info("Finishing deposit SAL method get total by category with total: " + str(total))
                return total

    def get_total_by_month(self, user_id: int, month: int, year: int) -> float:
        logging.info("Beginning Deposit SAL method get total by month with user ID: " + str(user_id) + " month: " +
                     str(month) + " and year: " + str(year))
        if type(user_id) is not int:
            logging.warning("Error in Deposit SAL method delete all deposits, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif type(month) is not int:
            logging.warning("Error in Deposit SAL method get total by month, month not an integer")
            raise CustomError("The month field must be an integer, please try again!")
        elif month not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            logging.warning("Error in Deposit SAL method get total by month, month not 1-12")
            raise CustomError("The month field must be an integer between 1 and 12, please try again!")
        elif type(year) is not int:
            logging.warning("Error in Deposit SAL method get total by month, year not an integer")
            raise CustomError("The year field must be an integer, please try again!")
        else:
            self.user_sao.get_user_by_id(user_id)
            deposits = self.get_all_deposits(user_id)
            total = 0.00
            for deposit in deposits:
                if deposit.date.month == month and deposit.date.year == year:
                    total = total + deposit.amount
            if total == 0.00 or total == 0:
                logging.warning("Error in Deposit SAL method get total by month, no deposits this month")
                raise CustomError("No deposits made during this time, please try again!")
            else:
                total = self.deposit_dao.get_total_by_month(month, year)
                logging.warning("Finishing Deposit SAL method get total by month with total: " + str(total))
                return total

    def get_total_by_year(self, user_id: int, year: int) -> float:
        logging.info("Beginning Deposit SAL method get total by year with user ID: " + str(user_id) + " and year: " +
                     str(year))
        if type(user_id) is not int:
            logging.warning("Error in Deposit SAL method get total by year, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif type(year) is not int:
            logging.warning("Error in Deposit SAL method get total by year, year not an integer")
            raise CustomError("The year field must be an integer, please try again!")
        else:
            self.user_sao.get_user_by_id(user_id)
            deposits = self.get_all_deposits(user_id)
            total = 0.00
            for deposit in deposits:
                if deposit.date.year == year:
                    total = total + deposit.amount
            if total == 0.00 or total == 0:
                logging.warning("Error in Deposit SAL method get total by month, no deposits this month")
                raise CustomError("No deposits made during this time, please try again!")
            else:
                total = self.deposit_dao.get_total_by_year(year)
                logging.warning("Finishing Deposit SAL method get total by month with total: " + str(total))
                return total

    def update_deposit(self, deposit: Deposit) -> bool:
        logging.info("Beginning SAL method update deposit with data: " + str(deposit.convert_to_dictionary()))
        if type(deposit.category_id) is not int:
            logging.warning("Error in SAL method update deposit, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif type(deposit.user_id) is not int:
            logging.warning("Error in SAL method update deposit, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif not isinstance(deposit.date, date):
            logging.warning("Error in SAL method update deposit, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif deposit.date == date(1, 1, 1):
            logging.warning("Error in SAL method update deposit, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(deposit.description) is not str:
            logging.warning("Error in SAL method update deposit, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif deposit.description == "":
            logging.warning("Error in SAL method update deposit, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(deposit.amount) is not float:
            logging.warning("Error in SAL method update deposit, amount not a float")
            raise CustomError("The amount field must be a float, please try again!")
        elif deposit.amount <= 0.00:
            logging.warning("Error in SAL method update deposit, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.user_sao.get_user_by_id(deposit.user_id)
            self.category_sao.get_category(deposit.category_id)
            self.get_deposit(deposit.deposit_id)
            result = self.deposit_dao.update_deposit(deposit)
            logging.info("Finishing SAL method update deposit")
            return result

    def delete_deposit(self, deposit_id: int) -> bool:
        logging.info("Beginning SAL method delete deposit with deposit ID: " + str(deposit_id))
        if type(deposit_id) is not int:
            logging.warning("Error in SAL method delete deposit, deposit ID not an integer")
            raise CustomError("The deposit ID field must be an integer, please try again!")
        else:
            self.get_deposit(deposit_id)
            result = self.deposit_dao.delete_deposit(deposit_id)
            logging.info("Finishing SAL method delete deposit")
            return result

    def delete_all_deposits(self, user_id: int) -> bool:
        logging.info("Beginning SAL method delete all deposits with user ID: " + str(user_id))
        if type(user_id) is not int:
            logging.warning("Error in SAL method delete all deposits, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        else:
            self.user_sao.get_user_by_id(user_id)
            result = self.deposit_dao.delete_all_deposits(user_id)
            logging.info("Finishing SAL method delete all deposits")
            return result
