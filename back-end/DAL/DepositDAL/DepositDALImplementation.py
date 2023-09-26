import logging
from typing import List

from DAL.DepositDAL.DepositDALInterface import DepositDALInterface
from Database.config import Connection
from Entities.Deposit import Deposit

class DepositDALImplementation(DepositDALInterface):

    def create_deposit(self, deposit: Deposit) -> Deposit:
        pass

    def get_all_deposits(self) -> List[Deposit]:
        pass

    def update_deposit(self, deposit: Deposit) -> Deposit:
        pass

    def delete_deposit(self, deposit_id: int) -> bool:
        pass
