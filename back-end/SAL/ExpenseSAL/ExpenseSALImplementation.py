import logging
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
        pass

    def get_expense(self, expense_id: int) -> Expense:
        pass

    def get_all_expenses(self) -> List[Expense]:
        pass

    def update_expense(self, expense: Expense) -> Expense:
        pass

    def delete_expense(self, expense_id: int) -> bool:
        pass
