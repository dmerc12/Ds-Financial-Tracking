from abc import ABC, abstractmethod
from typing import List

from Entities.Expense import Expense

class ExpenseDALInterface(ABC):

    @abstractmethod
    def create_expense(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def get_all_expenses(self) -> List[Expense]:
        pass

    @abstractmethod
    def update_expense(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def delete_expense(self, expense_id: int) -> bool:
        pass
