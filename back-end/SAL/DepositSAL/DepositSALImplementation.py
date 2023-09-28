import logging
from typing import List

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALInterface import DepositSALInterface
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

class DepositSALImplementation(DepositSALInterface):

    def __init__(self, deposit_dao: DepositDALImplementation):
        self.deposit_dao = deposit_dao

    def create_deposit(self, deposit: Deposit) -> Deposit:
        pass

    def get_deposit(self, deposit_id: int) -> Deposit:
        pass

    def get_all_deposits(self) -> List[Deposit]:
        pass

    def update_deposit(self, deposit: Deposit) -> Deposit:
        pass

    def delete_deposit(self, deposit_id: int) -> bool:
        pass
