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
    def get_all_expenses(self, user_id: int) -> List[Expense]:
        pass

    @abstractmethod
    def get_expenses_by_category(self, category_id: int) -> List[Expense]:
        pass

    @abstractmethod
    def get_expenses_by_date(self, date: str) -> List[Expense]:
        pass

    @abstractmethod
    def get_expenses_by_description_key_words(self, keywords: List[str]) -> List[Expense]:
        pass

    @abstractmethod
    def get_total_by_category(self, category_id: int) -> float:
        pass

    @abstractmethod
    def get_total_by_month(self, user_id: int, month: int, year: int) -> float:
        pass

    @abstractmethod
    def get_total_by_year(self, user_id: int, year: int) -> float:
        pass

    @abstractmethod
    def update_expense(self, expense: Expense) -> Expense:
        pass

    @abstractmethod
    def delete_expense(self, expense_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_expenses(self, user_id: int) -> bool:
        pass
