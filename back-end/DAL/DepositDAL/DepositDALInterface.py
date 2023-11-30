from abc import ABC, abstractmethod
from typing import List
from datetime import date
from Entities.Deposit import Deposit

class DepositDALInterface(ABC):

    @abstractmethod
    def create_deposit(self, deposit: Deposit) -> Deposit:
        pass

    @abstractmethod
    def get_deposit(self, deposit_id: int) -> Deposit:
        pass

    @abstractmethod
    def get_all_deposits(self, user_id: int) -> List[Deposit]:
        pass

    @abstractmethod
    def get_deposits_by_category(self, category_id: int) -> List[Deposit]:
        pass

    @abstractmethod
    def get_deposits_by_date(self, deposit_date: date) -> List[Deposit]:
        pass

    @abstractmethod
    def get_deposits_by_description_key_words(self, keywords: List[str]) -> List[Deposit]:
        pass

    @abstractmethod
    def get_total_by_category(self, category_id: int) -> float:
        pass

    @abstractmethod
    def get_total_by_month(self, month: int, year: int) -> float:
        pass

    @abstractmethod
    def get_total_by_year(self, year: int) -> float:
        pass

    @abstractmethod
    def update_deposit(self, deposit: Deposit) -> bool:
        pass

    @abstractmethod
    def delete_deposit(self, deposit_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_deposits(self, user_id: int) -> bool:
        pass
