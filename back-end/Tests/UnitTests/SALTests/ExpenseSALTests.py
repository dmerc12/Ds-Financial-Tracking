import unittest.mock as mock
from datetime import datetime, timedelta

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.Expense import Expense
from Entities.CustomError import CustomError

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

successful_expense = Expense(0, -1, str(datetime.now().date()), 'test description', 5.00)
current_expense_id = 1
updated_expense = Expense(current_expense_id, -1, str(datetime.now().date() - timedelta(days=7, weeks=13)),
                          'updated description', 10.00)

def test_sal_create_expense_category_id_not_integer():
    try:
        test_expense = Expense(0, '', str(datetime.now().date()), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_create_expense_category_not_found():
    try:
        test_expense = Expense(0, -579356834926, str(datetime.now().date()), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_create_expense_date_not_string():
    try:
        test_expense = Expense(0, -1, datetime.now().date(), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a string, please try again!"

def test_sal_create_expense_date_empty():
    try:
        test_expense = Expense(0, -1, '', 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_sal_create_expense_description_not_string():
    try:
        test_expense = Expense(0, -1, str(datetime.now().date()), 5, 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_sal_create_expense_description_empty():
    try:
        test_expense = Expense(0, -1, str(datetime.now().date()), '', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_sal_create_expense_amount_not_float():
    try:
        test_expense = Expense(0, -1, str(datetime.now().date()), 'description', '10.00')
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_sal_create_expense_amount_negative_or_0():
    try:
        test_expense = Expense(0, -1, str(datetime.now().date()), 'description', -10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_sal_create_expense_success():
    result = expense_sao.create_expense(successful_expense)
    assert result.expense_id != 0

def test_sal_get_expense_id_not_integer():
    try:
        expense_sao.get_expense('')
        assert False
    except CustomError as error:
        assert str(error) == "The expense ID field must be an integer, please try again!"

def test_sal_get_expense_not_found():
    try:
        expense_sao.get_expense(-3869529838)
        assert False
    except CustomError as error:
        assert str(error) == "Expense not found, please try again!"

def test_sal_get_expense_success():
    result = expense_sao.get_expense(current_expense_id)
    assert result is not None

def test_sal_get_all_expenses_none_found():
    with mock.patch.object(expense_sao.expense_dao, 'get_all_expenses', return_value=[]):
        try:
            expense_sao.get_all_expenses()
            assert False
        except CustomError as error:
            assert str(error) == "No expenses found, please try again!"

def test_sal_get_all_expenses_success():
    result = expense_sao.get_all_expenses()
    assert len(result) > 0

def test_sal_update_expense_category_id_not_integer():
    try:
        test_expense = Expense(current_expense_id, '', str(datetime.now().date()), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_sal_update_expense_category_not_found():
    try:
        test_expense = Expense(current_expense_id, -1578576467, str(datetime.now().date()), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_sal_update_expense_date_not_string():
    try:
        test_expense = Expense(current_expense_id, -1, datetime.now().date(), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a string, please try again!"

def test_sal_update_expense_date_empty():
    try:
        test_expense = Expense(current_expense_id, -1, '', 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_sal_update_expense_description_not_string():
    try:
        test_expense = Expense(current_expense_id, -1, str(datetime.now().date()), 6, 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_sal_update_expense_description_empty():
    try:
        test_expense = Expense(current_expense_id, -1, str(datetime.now().date()), '', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_sal_update_expense_amount_not_float():
    try:
        test_expense = Expense(current_expense_id, -1, str(datetime.now().date()), 'test description', '5.00')
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_sal_update_expense_amount_negative_or_0():
    try:
        test_expense = Expense(current_expense_id, -1, str(datetime.now().date()), 'test description', -5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_sal_update_expense_success():
    result = expense_sao.update_expense(updated_expense)
    assert result.date != successful_expense.date and result.description != successful_expense.description and \
           result.amount != successful_expense.amount

def test_sal_delete_expense_not_found():
    try:
        expense_sao.delete_expense(-37542792)
        assert False
    except CustomError as error:
        assert str(error) == "Expense not found, please try again!"

def test_sal_delete_expense_id_not_integer():
    try:
        expense_sao.delete_expense('')
        assert False
    except CustomError as error:
        assert str(error) == "The expense ID field must be an integer, please try again!"

def test_sal_delete_expense_success():
    result = expense_sao.delete_expense(current_expense_id)
    assert result
