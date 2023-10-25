import logging
from typing import List

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALInterface import DepositSALInterface
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

class DepositSALImplementation(DepositSALInterface):

    def __init__(self, deposit_dao: DepositDALImplementation, category_sao: CategorySALImplementation):
        self.deposit_dao = deposit_dao
        self.category_sao = category_sao

    def create_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning SAL method create deposit with data: " + str(deposit.convert_to_dictionary()))
        if type(deposit.category_id) != int:
            logging.warning("Error in SAL method create deposit, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif deposit.category_id == 0:
            logging.warning("Error in SAL method create deposit, category ID not set")
            raise CustomError("A category must be set, please try again!")
        elif type(deposit.date) != str:
            logging.warning("Error in SAL method create deposit, date not a string")
            raise CustomError("The date field must be a string, please try again!")
        elif deposit.date == "":
            logging.warning("Error in SAL method create deposit, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(deposit.description) != str:
            logging.warning("Error in SAL method create deposit, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif deposit.description == "":
            logging.warning("Error in SAL method create deposit, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif deposit.amount <= 0.00:
            logging.warning("Error in SAL method create deposit, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.category_sao.get_category(deposit.category_id)
            result = self.deposit_dao.create_deposit(deposit)
            logging.info("Finishing SAL method create deposit with result: " + str(deposit.convert_to_dictionary()))
            return result

    def get_deposit(self, deposit_id: int) -> Deposit:
        logging.info("Beginning SAL method get deposit with deposit ID: " + str(deposit_id))
        if type(deposit_id) != int:
            logging.warning("Error in SAL method get deposit, deposit ID not an integer")
            raise CustomError("The deposit ID field must be an integer, please try again!")
        else:
            deposit = self.deposit_dao.get_deposit(deposit_id)
            if deposit.deposit_id == 0 and deposit.category_id == 0 and deposit.date == "" and \
               deposit.description == "" and deposit.amount == 0.00:
                logging.warning("Error in SAL method get deposit, deposit not found")
                raise CustomError("Deposit not found, please try again!")
            else:
                logging.info("Finishing SAL method get deposit with result: " + str(deposit.convert_to_dictionary()))
                return deposit

    def get_all_deposits(self) -> List[Deposit]:
        logging.info("Beginning SAL method get all deposits")
        deposits = self.deposit_dao.get_all_deposits()
        if len(deposits) == 0:
            logging.warning("Error in SAL method get all categories, none found")
            raise CustomError("No deposits found, please try again!")
        else:
            logging.info("Finishing SAL method get all deposits")
            return deposits

    def update_deposit(self, deposit: Deposit) -> Deposit:
        logging.info("Beginning SAL method update deposit with data: " + str(deposit.convert_to_dictionary()))
        if type(deposit.category_id) != int:
            logging.warning("Error in SAL method update deposit, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif type(deposit.date) != str:
            logging.warning("Error in SAL method update deposit, date not a string")
            raise CustomError("The date field must be a string, please try again!")
        elif deposit.date == "":
            logging.warning("Error in SAL method update deposit, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(deposit.description) != str:
            logging.warning("Error in SAL method update deposit, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif deposit.description == "":
            logging.warning("Error in SAL method update deposit, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(deposit.amount) != float:
            logging.warning("Error in SAL method update deposit, amount not a float")
            raise CustomError("The amount field must be a float, please try again!")
        elif deposit.amount <= 0.00:
            logging.warning("Error in SAL method update deposit, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.category_sao.get_category(deposit.category_id)
            self.get_deposit(deposit.deposit_id)
            result = self.deposit_dao.update_deposit(deposit)
            logging.info("Finishing SAL method update deposit with result: " + str(result.convert_to_dictionary()))
            return result

    def delete_deposit(self, deposit_id: int) -> bool:
        logging.info("Beginning SAL method delete deposit with deposit ID: " + str(deposit_id))
        if type(deposit_id) != int:
            logging.warning("Error in SAL method delete deposit, deposit ID not an integer")
            raise CustomError("The deposit ID field must be an integer, please try again!")
        else:
            self.get_deposit(deposit_id)
            result = self.deposit_dao.delete_deposit(deposit_id)
            logging.info("Finishing SAL method delete deposit")
            return result
