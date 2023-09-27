import logging
from typing import List

from DAL.ExpenseDAL.ExpenseDALInterface import ExpenseDALInterface
from Database.config import Connection
from Entities.Expense import Expense


class ExpenseDALImplementation(ExpenseDALInterface):

    def create_expense(self, expense: Expense) -> Expense:
        pass

    def get_all_expenses(self) -> List[Expense]:
        pass

    def update_expense(self, expense: Expense) -> Expense:
        pass

    def delete_expense(self, expense_id: int) -> bool:
        pass
