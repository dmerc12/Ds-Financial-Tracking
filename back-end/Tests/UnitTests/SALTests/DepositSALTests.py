from datetime import datetime, timedelta

from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao)

successful_deposit = Deposit(0, -1, str(datetime.now()), 'test description', 5.00)
current_deposit_id = 1
updated_deposit = Deposit(current_deposit_id, -1, str(datetime.now() - timedelta(hours=7, minutes=13, seconds=34)),
                          'updated description', 10.00)

def test_sal_create_deposit_category_id_not_integer():
    pass

def test_sal_create_deposit_category_not_found():
    pass

def test_sal_create_deposit_date_not_string():
    pass

def test_sal_create_deposit_date_empty():
    pass

def test_sal_create_deposit_description_not_string():
    pass

def test_sal_create_deposit_description_empty():
    pass

def test_sal_create_deposit_amount_not_float():
    pass

def test_sal_create_deposit_amount_negative_or_0():
    pass

def test_sal_create_deposit_success():
    pass

def test_sal_get_deposit_id_not_integer():
    pass

def test_sal_get_deposit_not_found():
    pass

def test_sal_get_deposit_success():
    pass

def test_sal_get_all_deposits_none_found():
    pass

def test_sal_get_all_deposits_success():
    pass

def test_sal_update_deposit_nothing_changed():
    pass

def test_sal_update_deposit_category_id_not_integer():
    pass

def test_sal_update_deposit_category_not_found():
    pass

def test_sal_update_deposit_date_not_string():
    pass

def test_sal_update_deposit_date_empty():
    pass

def test_sal_update_deposit_description_not_string():
    pass

def test_sal_update_deposit_description_empty():
    pass

def test_sal_update_deposit_amount_not_float():
    pass

def test_sal_update_deposit_amount_negative_or_0():
    pass

def test_sal_update_deposit_success():
    pass

def test_sal_delete_deposit_not_found():
    pass

def test_sal_delete_deposit_id_not_integer():
    pass

def test_sal_delete_deposit_success():
    pass
