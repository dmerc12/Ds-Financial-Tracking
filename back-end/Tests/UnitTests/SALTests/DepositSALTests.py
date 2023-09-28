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
    try:
        pass
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_create_deposit_category_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_create_deposit_date_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The date field must be a string, please try again!"

def test_sal_create_deposit_date_empty():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_sal_create_deposit_description_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_sal_create_deposit_description_empty():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_sal_create_deposit_amount_not_float():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_sal_create_deposit_amount_negative_or_0():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_sal_create_deposit_success():
    pass

def test_sal_get_deposit_id_not_integer():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The deposit ID field must be an integer, please try again!"

def test_sal_get_deposit_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == "Deposit not found, please try again!"

def test_sal_get_deposit_success():
    pass

def test_sal_get_all_deposits_none_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == "No deposits found, please try again!"

def test_sal_get_all_deposits_success():
    pass

def test_sal_update_deposit_nothing_changed():
    try:
        pass
    except CustomError as error:
        assert str(error) == "Nothing changed, please try again!"

def test_sal_update_deposit_category_id_not_integer():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_update_deposit_category_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_update_deposit_date_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The date field must be a string, please try again!"

def test_sal_update_deposit_date_empty():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_sal_update_deposit_description_not_string():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_sal_update_deposit_description_empty():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_sal_update_deposit_amount_not_float():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_sal_update_deposit_amount_negative_or_0():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_sal_update_deposit_success():
    pass

def test_sal_delete_deposit_not_found():
    try:
        pass
    except CustomError as error:
        assert str(error) == "Deposit not found, please try again!"

def test_sal_delete_deposit_id_not_integer():
    try:
        pass
    except CustomError as error:
        assert str(error) == "The deposit ID field must be an integer, please try again!"

def test_sal_delete_deposit_success():
    pass
