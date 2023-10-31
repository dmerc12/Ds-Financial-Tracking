from abc import ABC, abstractmethod
from typing import List

from Entities.Expense import Expense

class ExpenseSALInterface(ABC):

    @abstractmethod
    def create_expense(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def get_expense(self, expense_id: int) -> Expense:
        pass

    @abstractmethod
    def get_all_expenses(self) -> List[Expense]:
        pass

    @abstractmethod
    def get_expenses_by_category(self, category_id: int) -> List[Expense]:
        pass

    @abstractmethod
    def get_expenses_by_date(self, date: str) -> List[Expense]:
        pass

    @abstractmethod
    def update_expense(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def delete_expense(self, expense_id: int) -> bool:
        pass
