from abc import ABC, abstractmethod
from typing import List

from Entities.Deposit import Deposit

class DepositDALInterface(ABC):

    @abstractmethod
    def create_deposit(self, deposit: Deposit) -> Deposit:
        pass

    @abstractmethod
    def get_deposit(self, deposit_id: int) -> Deposit:
        pass

    @abstractmethod
    def get_all_deposits(self) -> List[Deposit]:
        pass

    @abstractmethod
    def update_deposit(self, deposit: Deposit) -> Deposit:
        pass

    @abstractmethod
    def delete_deposit(self, deposit_id: int) -> bool:
        pass
