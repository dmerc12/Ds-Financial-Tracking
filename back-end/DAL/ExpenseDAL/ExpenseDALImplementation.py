import logging
from datetime import date
from typing import List

from DAL.ExpenseDAL.ExpenseDALInterface import ExpenseDALInterface
from Database.config import Connection
from Entities.Expense import Expense


class ExpenseDALImplementation(ExpenseDALInterface):

    def create_expense(self, expense: Expense) -> Expense:
        logging.info("Beginning DAL method create expense with data: " + str(expense.convert_to_dictionary()))
        sql = "INSERT INTO financial_tracker.Expense (category_id, date, description, amount) VALUES " \
              "(%s, %s, %s, %s) RETURNING expense_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense.category_id, expense.date, expense.description, expense.amount))
        expense.expense_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create expense with result: " + str(expense.convert_to_dictionary()))
        return expense

    def get_expense(self, expense_id: int) -> Expense:
        logging.info("Beginning DAL method get expense with expense ID: " + str(expense_id))
        sql = "SELECT * FROM financial_tracker.Expense WHERE expense_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense_id,))
        expense_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if expense_info is None:
            expense = Expense(0, 0, '', '', 0.00)
            logging.info("Finishing DAL method get expense, expense not found")
            return expense
        else:
            expense = Expense(*expense_info)
            logging.info("Finishing DAL method get expense with expense: " + str(expense.convert_to_dictionary()))
            return expense

    def get_all_expenses(self) -> List[Expense]:
        logging.info("Beginning DAL method get all expenses;")
        sql = "SELECT * FROM financial_tracker.Expense"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        expense_records = cursor.fetchall()
        expenses = []
        for expense in expense_records:
            expense = Expense(
                expense_id=expense[0],
                category_id=expense[4],
                expense_date=expense[1],
                description=expense[2],
                amount=expense[3]
            )
            expenses.append(expense)
            logging.info("Finishing DAL method get all expenses with result: " +
                         str(expense.convert_to_dictionary()))
        cursor.close()
        connection.commit()
        connection.close()
        return expenses

    def get_expenses_by_category(self, category_id: int) -> List[Expense]:
        logging.info("Beginning DAL method get expenses by category with category ID: " + str(category_id))
        sql = "SELECT * from financial_tracker.Expense WHERE category_id=?;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        expense_records = cursor.fetchall()
        expenses = []
        for expense in expense_records:
            expense = Expense(
                expense_id=expense[0],
                category_id=expense[4],
                expense_date=expense[1],
                description=expense[2],
                amount=expense[3]
            )
            expenses.append(expense)
            logging.info("Finishing DAL method get all expenses by category with result: " +
                         str(expense.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return expenses

    def get_expenses_by_date(self, expense_date: date) -> List[Expense]:
        logging.info("Beginning DAL method get expenses by date with date: " + str(expense_date))
        sql = "SELECT * from financial_tracker.Expense WHERE date=?;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (date,))
        expense_records = cursor.fetchall()
        expenses = []
        for expense in expense_records:
            expense = Expense(
                expense_id=expense[0],
                category_id=expense[4],
                expense_date=expense[1],
                description=expense[2],
                amount=expense[3]
            )
            expenses.append(expense)
            logging.info(
                "Finishing DAL method get all expenses by date with result: " + str(expense.convert_to_dictionary()))
        cursor.close()
        connection.close()
        return expenses

    def update_expense(self, expense: Expense) -> Expense:
        logging.info("Beginning DAL method update expense with data: " + str(expense.convert_to_dictionary()))
        sql = "UPDATE financial_tracker.Expense SET category_id=%s, date=%s, description=%s, amount=%s WHERE " \
              "expense_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense.category_id, expense.date, expense.description, expense.amount,
                             expense.expense_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update expense with result: " + str(expense.convert_to_dictionary()))
        return expense

    def delete_expense(self, expense_id: int) -> bool:
        logging.info("Beginning DAL method delete expense with expense ID: " + str(expense_id))
        sql = "DELETE FROM financial_tracker.Expense WHERE expense_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete expense")
        return True
