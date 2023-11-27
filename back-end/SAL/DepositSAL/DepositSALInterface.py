from abc import ABC, abstractmethod
from typing import List

from Entities.Deposit import Deposit

class DepositSALInterface(ABC):

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
    def get_deposits_by_date(self, date: str) -> List[Deposit]:
        pass

    @abstractmethod
    def get_deposits_total_by_category(self, category_id: int) -> float:
        pass

    @abstractmethod
    def get_deposits_total_by_month(self) -> float:
        pass

    @abstractmethod
    def get_deposits_total_by_year(self) -> float:
        pass

    @abstractmethod
    def search_deposits_by_description_key_words(self) -> List[Deposit]:
        pass

    @abstractmethod
    def update_deposit(self, deposit: Deposit) -> Deposit:
        pass

    @abstractmethod
    def delete_deposit(self, deposit_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_deposits(self, user_id: int) -> bool:
        pass
