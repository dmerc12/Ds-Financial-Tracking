from datetime import datetime

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from Entities.Deposit import Deposit

deposit_dao = DepositDALImplementation()
test_deposit = Deposit(0, 1, str(datetime.now()), 'test description', 25.00)
current_deposit_id = 1
updated_deposit = Deposit(current_deposit_id, test_deposit.category_id, test_deposit.date, 'updated', 50.00)

def test_create_deposit_success():
    result = deposit_dao.create_deposit(test_deposit)
    assert result.deposit_id != 0

def test_get_all_deposits_success():
    result = deposit_dao.get_all_deposits()
    assert len(result) > 0

def test_update_deposit_success():
    result = deposit_dao.update_deposit(updated_deposit)
    assert result.date != test_deposit.date and result.description != test_deposit.description and \
           result.amount != test_deposit.amount

def test_delete_deposit_success():
    result = deposit_dao.delete_deposit(current_deposit_id)
    assert result
