from datetime import datetime, timedelta

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from Entities.Deposit import Deposit

deposit_dao = DepositDALImplementation()
test_deposit = Deposit(0, -1, -1, datetime.now(), 'test description', 25.00)
current_deposit_id = 1
updated_deposit = Deposit(current_deposit_id, test_deposit.user_id, test_deposit.category_id,
                          datetime.now().date() - timedelta(days=38), 'updated', 50.00)

def test_create_deposit_success():
    result = deposit_dao.create_deposit(test_deposit)
    assert result.deposit_id != 0

def test_get_deposit_success():
    result = deposit_dao.get_deposit(current_deposit_id)
    assert result is not None

def test_get_all_deposits_success():
    result = deposit_dao.get_all_deposits(test_deposit.user_id)
    assert len(result) > 0

def test_get_deposits_by_category_success():
    result = deposit_dao.get_deposits_by_category(test_deposit.category_id)
    assert len(result) > 0

def test_get_deposits_by_date_success():
    result = deposit_dao.get_deposits_by_date(test_deposit.date)
    assert len(result) > 0

def test_get_deposits_by_description_key_words_success():
    result = deposit_dao.get_deposits_by_description_key_words(["test", "description"])
    assert len(result) > 0

def test_get_total_by_category_success():
    result = deposit_dao.get_total_by_category(test_deposit.category_id)
    assert result != 0.00

def test_get_total_by_month_success():
    result = deposit_dao.get_total_by_month(test_deposit.date.month, test_deposit.date.year)
    assert result != 0.00

def test_get_total_by_year_success():
    result = deposit_dao.get_total_by_year(test_deposit.date.year)
    assert result != 0.00

def test_update_deposit_success():
    result = deposit_dao.update_deposit(updated_deposit)
    assert result

def test_delete_deposit_success():
    result = deposit_dao.delete_deposit(current_deposit_id)
    assert result

def test_delete_all_deposits_success():
    result = deposit_dao.delete_all_deposits(-2)
    assert result
