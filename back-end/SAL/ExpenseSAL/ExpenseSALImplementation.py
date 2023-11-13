import logging
from datetime import date
from typing import List

from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALInterface import ExpenseSALInterface
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Expense import Expense
from Entities.CustomError import CustomError


class ExpenseSALImplementation(ExpenseSALInterface):

    def __init__(self, expense_dao: ExpenseDALImplementation, category_sao: CategorySALImplementation):
        self.expense_dao = expense_dao
        self.category_sao = category_sao

    def create_expense(self, expense: Expense) -> Expense:
        logging.info("Beginning SAL method create expense with data: " + str(expense.convert_to_dictionary()))
        if type(expense.category_id) is not int:
            logging.warning("Error in SAL method create expense, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif expense.category_id == 0:
            logging.warning("Error in SAL method create expense, category ID not set")
            raise CustomError("A category must be set, please try again!")
        elif not isinstance(expense.date, date):
            logging.warning("Error in SAL method create expense, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif expense.date == date(1900, 1, 1):
            logging.warning("Error in SAL method create expense, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(expense.description) is not str:
            logging.warning("Error in SAL method create expense, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif expense.description == "":
            logging.warning("Error in SAL method create expense, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(expense.amount) is not float:
            logging.warning("Error in SAL method create expense, amount not a float")
            raise CustomError("The amount field must be a float, please try again!")
        elif expense.amount <= 0.00:
            logging.warning("Error in SAL method create expense, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.category_sao.get_category(expense.category_id)
            result = self.expense_dao.create_expense(expense)
            logging.info("Finishing SAL method create expense with result: " + str(result.convert_to_dictionary()))
            return result

    def get_expense(self, expense_id: int) -> Expense:
        logging.info("Beginning SAL method get expense with expense ID: " + str(expense_id))
        if type(expense_id) is not int:
            logging.warning("Error in SAL method get expense, expense ID not an integer")
            raise CustomError("The expense ID field must be an integer, please try again!")
        else:
            expense = self.expense_dao.get_expense(expense_id)
            if (expense.expense_id == 0 and expense.category_id == 0 and expense.date ==
                    date(1900, 1, 1) and expense.description == '' and expense.amount == 0.00):
                logging.warning("Error in SAL method get expense, expense not found")
                raise CustomError("Expense not found, please try again!")
            else:
                logging.info("Finishing SAL method get expense with result: " + str(expense.convert_to_dictionary()))
                return expense

    def get_all_expenses(self, user_id: int) -> List[Expense]:
        logging.info("Beginning SAL method get all expenses")
        expenses = self.expense_dao.get_all_expenses(user_id)
        if len(expenses) == 0:
            logging.warning("Error in SAL method get all expenses, none found")
            raise CustomError("No expenses found, please try again!")
        else:
            logging.info("Finishing SAL method get all expenses")
            return expenses

    def get_expenses_by_category(self, category_id: int) -> List[Expense]:
        logging.info("Beginning SAL method get expenses by category with category ID: " + str(category_id))
        if type(category_id) is not int:
            logging.warning("Error in SAL method get expenses by category, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        else:
            self.category_sao.get_category(category_id)
            expenses = self.expense_dao.get_expenses_by_category(category_id)
            if len(expenses) == 0:
                logging.warning("Error in SAL method get expenses by category, none found")
                raise CustomError("No expenses found, please try again!")
            else:
                logging.info("Finishing SAL method get expenses by category")
                return expenses

    def get_expenses_by_date(self, expense_date: date) -> List[Expense]:
        logging.info("Beginning SAL method get expenses by date with date: " + str(expense_date))
        if not isinstance(expense_date, date):
            logging.warning("Error in SAL method create expense, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif expense_date == date(1900, 1, 1):
            logging.warning("Error in SAL method get expenses by date, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        else:
            expenses = self.expense_dao.get_expenses_by_date(expense_date)
            if len(expenses) == 0:
                logging.warning("Error in SAL method get expenses by date, none found")
                raise CustomError("No expenses found, please try again!")
            else:
                logging.info("Finishing SAL method get expenses by date")
                return expenses

    def update_expense(self, expense: Expense) -> Expense:
        logging.info("Beginning SAL method update expense with data: " + str(expense.convert_to_dictionary()))
        if type(expense.category_id) is not int:
            logging.warning("Error in SAL method update expense, category ID not an integer")
            raise CustomError("The category ID field must be an integer, please try again!")
        elif not isinstance(expense.date, date):
            logging.warning("Error in SAL method update expense, date not a date")
            raise CustomError("The date field must be a date, please try again!")
        elif expense.date == date(1900, 1, 1):
            logging.warning("Error in SAL method update expense, date empty")
            raise CustomError("The date field cannot be left empty, please try again!")
        elif type(expense.description) is not str:
            logging.warning("Error in SAL method update expense, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif expense.description == "":
            logging.warning("Error in SAL method update expense, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(expense.amount) is not float:
            logging.warning("Error in SAL method update expense, amount not a float")
            raise CustomError("The amount field must be a float, please try again!")
        elif expense.amount <= 0.00:
            logging.warning("Error in SAL method update expense, amount negative or 0.00")
            raise CustomError("The amount field must be positive and cannot be 0.00, please try again!")
        else:
            self.category_sao.get_category(expense.category_id)
            self.get_expense(expense.expense_id)
            result = self.expense_dao.update_expense(expense)
            logging.info("Finishing SAL method update expense with result: " + str(result.convert_to_dictionary()))
            return result

    def delete_expense(self, expense_id: int) -> bool:
        logging.info("Beginning SAL method delete expense with expense ID: " + str(expense_id))
        if type(expense_id) is not int:
            logging.warning("Error in SAL method delete expense, expense ID not an integer")
            raise CustomError("The expense ID field must be an integer, please try again!")
        else:
            self.get_expense(expense_id)
            result = self.expense_dao.delete_expense(expense_id)
            logging.info("Finishing SAL method delete expense")
            return result
