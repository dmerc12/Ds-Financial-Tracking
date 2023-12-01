import logging
from typing import List
from datetime import date

from DAL.ExpenseDAL.ExpenseDALInterface import ExpenseDALInterface
from Database.config import Connection
from Entities.Expense import Expense


class ExpenseDALImplementation(ExpenseDALInterface):

    def create_expense(self, expense: Expense) -> Expense:
        logging.info("Beginning DAL method create expense with data: " + str(expense.convert_to_dictionary()))
        sql = "INSERT INTO financial_tracker.Expense (user_id, category_id, date, description, amount) VALUES " \
              "(%s, %s, %s, %s, %s) RETURNING expense_id;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense.user_id, expense.category_id, expense.date, expense.description, expense.amount))
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
            expense = Expense(0, 0, 0, date(1, 1, 1), '', 0.00)
            logging.info("Finishing DAL method get expense, expense not found")
            return expense
        else:
            expense = Expense(*expense_info)
            logging.info("Finishing DAL method get expense with expense: " + str(expense.convert_to_dictionary()))
            return expense

    def get_all_expenses(self, user_id: int) -> List[Expense]:
        logging.info("Beginning DAL method get all expenses with user ID: " + str(user_id))
        sql = "SELECT * FROM financial_tracker.Expense where user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        expense_records = cursor.fetchall()
        cursor.close()
        connection.close()
        expenses = []
        for expense in expense_records:
            expense = Expense(*expense)
            expenses.append(expense)
            logging.info("Finishing DAL method get all expenses with result: " +
                         str(expense.convert_to_dictionary()))
        return expenses

    def get_expenses_by_category(self, category_id: int) -> List[Expense]:
        logging.info("Beginning DAL method get expenses by category with category ID: " + str(category_id))
        sql = "SELECT * from financial_tracker.Expense WHERE category_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        expense_records = cursor.fetchall()
        cursor.close()
        connection.close()
        expenses = []
        for expense in expense_records:
            expense = Expense(*expense)
            expenses.append(expense)
            logging.info("Finishing DAL method get expenses by category with result: " +
                         str(expense.convert_to_dictionary()))
        return expenses

    def get_expenses_by_date(self, expense_date: date) -> List[Expense]:
        logging.info("Beginning DAL method get expenses by date with date: " + str(expense_date))
        sql = "SELECT * from financial_tracker.Expense WHERE EXTRACT(DAY FROM date)=%s AND EXTRACT(MONTH FROM " \
              "date)=%s AND EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (expense_date.day, expense_date.month, expense_date.year))
        expense_records = cursor.fetchall()
        cursor.close()
        connection.close()
        expenses = []
        for expense in expense_records:
            expense = Expense(*expense)
            expenses.append(expense)
            logging.info("Finishing DAL method get expenses by date with result: " +
                         str(expense.convert_to_dictionary()))
        return expenses


    def get_expenses_by_description_key_words(self, keywords: List[str]) -> List[Expense]:
        logging.info("Beginning Expense DAL method get expenses by description key words with keywords: " +
                     str(keyword for keyword in keywords))
        placeholders = ", ".join(['%s'] * len(keywords))
        sql = f"SELECT * FROM financial_tracker.Expense WHERE description LIKE ANY(ARRAY[{placeholders}]);"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, tuple(f"%{keyword}%" for keyword in keywords))
        expense_records = cursor.fetchall()
        cursor.close()
        connection.close()
        expenses = []
        for expense in expense_records:
            expense = Expense(*expense)
            expenses.append(expense)
            logging.info("Finishing DAL method get expenses by description keywords with result: " +
                         str(expense.convert_to_dictionary()))
        return expenses

    def get_total_by_category(self, category_id: int) -> float:
        logging.info("Beginning Expense DAL method get total by category with category ID: " + str(category_id))
        sql = "SELECT SUM(amount) FROM financial_tracker.Expense WHERE category_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (category_id,))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        logging.info("Finishing Expense DAL method get total by category with total: " + str(total))
        return total

    def get_total_by_month(self, month: int, year: int) -> float:
        logging.info("Beginning Expense DAL method get total by month with month: " + str(month) + " and year: " +
                     str(year))
        sql = "SELECT SUM(amount) FROM financial_tracker.Expense WHERE EXTRACT(MONTH FROM date)=%s AND " \
              "EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (month, year))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        logging.info("Finishing Expense DAL method get total by month with total: " + str(total))
        return total

    def get_total_by_year(self, year: int) -> float:
        logging.info("Beginning Expense DAL method get total by year with year: " + str(year))
        sql = "SELECT SUM(amount) FROM financial_tracker.Expense WHERE EXTRACT(YEAR FROM date)=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (year,))
        total = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        logging.info("Finishing Expense DAL method get total by year with total: " + str(total))
        return total

    def update_expense(self, expense: Expense) -> bool:
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
        logging.info("Finishing DAL method update expense")
        return True

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

    def delete_all_expenses(self, user_id: int) -> bool:
        logging.info("Beginning DAL method delete all expenses with user ID: " + str(user_id))
        sql = "DELETE FROM financial_tracker.Expense WHERE user_id=%s;"
        connection = Connection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete all expenses")
        return True
