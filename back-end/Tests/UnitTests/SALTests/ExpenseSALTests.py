import unittest.mock as mock
from datetime import datetime, timedelta, date

from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.CustomError import CustomError
from Entities.Expense import Expense

expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao)

successful_expense = Expense(0, -1, -1, datetime.now().date(), 'test description', 5.00)
current_expense_id = 1
updated_expense = Expense(current_expense_id, -1, -1, datetime.now().date() - timedelta(days=7),
                          'updated description', 10.00)

def test_create_expense_category_id_not_integer():
    try:
        test_expense = Expense(0, -1, '', datetime.now().date(), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_create_expense_category_not_set():
    try:
        test_expense = Expense(0, -1, 0, datetime.now().date(), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "A category must be set, please try again!"

def test_create_expense_category_not_found():
    try:
        test_expense = Expense(0, -1, -579356834926, datetime.now().date(), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_create_expense_date_not_date():
    try:
        test_expense = Expense(0, -1, -1, str(datetime.now().date()), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a date, please try again!"

def test_create_expense_date_empty():
    try:
        test_expense = Expense(0, -1, -1, date(1900, 1, 1), 'description', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_create_expense_description_not_string():
    try:
        test_expense = Expense(0, -1, -1, datetime.now().date(), 5, 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_create_expense_description_empty():
    try:
        test_expense = Expense(0, -1, -1, datetime.now().date(), '', 10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_create_expense_amount_not_float():
    try:
        test_expense = Expense(0, -1, -1, datetime.now().date(), 'description', '10.00')
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_create_expense_amount_negative_or_0():
    try:
        test_expense = Expense(0, -1, -1, datetime.now().date(), 'description', -10.00)
        expense_sao.create_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_create_expense_success():
    result = expense_sao.create_expense(successful_expense)
    assert result.expense_id != 0

def test_get_expense_id_not_integer():
    try:
        expense_sao.get_expense('')
        assert False
    except CustomError as error:
        assert str(error) == "The expense ID field must be an integer, please try again!"

def test_get_expense_not_found():
    try:
        expense_sao.get_expense(-3869529838)
        assert False
    except CustomError as error:
        assert str(error) == "Expense not found, please try again!"

def test_get_expense_success():
    result = expense_sao.get_expense(current_expense_id)
    assert result is not None

def test_get_all_expenses_none_found():
    with mock.patch.object(expense_sao.expense_dao, 'get_all_expenses', return_value=[]):
        try:
            expense_sao.get_all_expenses(-2)
            assert False
        except CustomError as error:
            assert str(error) == "No expenses found, please try again!"

def test_get_all_expenses_success():
    result = expense_sao.get_all_expenses(successful_expense.user_id)
    assert len(result) > 0

def test_get_expenses_by_category_category_id_not_integer():
    try:
        expense_sao.get_expenses_by_category("nope")
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_get_expenses_by_category_none_found():
    try:
        expense_sao.get_expenses_by_category(-2)
        assert False
    except CustomError as error:
        assert str(error) == "No expenses found, please try again!"

def test_get_expenses_by_category_category_not_found():
    try:
        expense_sao.get_expenses_by_category(-5734932032648)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_get_expenses_by_category_success():
    result = expense_sao.get_expenses_by_category(successful_expense.category_id)
    assert len(result) > 0

def test_get_expenses_by_date_date_not_date():
    try:
        expense_sao.get_expenses_by_date(12537843)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a date, please try again!"

def test_get_expenses_by_date_date_empty():
    try:
        expense_sao.get_expenses_by_date(date(1900, 1, 1))
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_get_expenses_by_date_none_found():
    try:
        expense_sao.get_expenses_by_date(date(1972, 3, 1))
        assert False
    except CustomError as error:
        assert str(error) == "No expenses found, please try again!"

def test_get_expenses_by_date_success():
    result = expense_sao.get_expenses_by_date(successful_expense.date)
    assert len(result) > 0


def test_get_expenses_total_by_category_success():
    pass


def test_get_expenses_total_by_month_success():
    pass


def test_get_expenses_total_by_year_success():
    pass


def test_get_expenses_by_description_key_words_success():
    pass

def test_update_expense_category_id_not_integer():
    try:
        test_expense = Expense(current_expense_id, -1, '', datetime.now().date(), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The category ID field must be an integer, please try again!"

def test_update_expense_category_not_found():
    try:
        test_expense = Expense(current_expense_id, -1, -1578576467, datetime.now().date(), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "Category not found, please try again!"

def test_update_expense_date_not_date():
    try:
        test_expense = Expense(current_expense_id, -1, -1, str(datetime.now().date()), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field must be a date, please try again!"

def test_update_expense_date_empty():
    try:
        test_expense = Expense(current_expense_id, -1, -1, date(1900, 1, 1), 'test description', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The date field cannot be left empty, please try again!"

def test_update_expense_description_not_string():
    try:
        test_expense = Expense(current_expense_id, -1, -1, datetime.now().date(), 6, 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field must be a string, please try again!"

def test_update_expense_description_empty():
    try:
        test_expense = Expense(current_expense_id, -1, -1, datetime.now().date(), '', 5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The description field cannot be left empty, please try again!"

def test_update_expense_amount_not_float():
    try:
        test_expense = Expense(current_expense_id, -1, -1, datetime.now().date(), 'test description', '5.00')
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be a float, please try again!"

def test_update_expense_amount_negative_or_0():
    try:
        test_expense = Expense(current_expense_id, -1, -1, datetime.now().date(), 'test description', -5.00)
        expense_sao.update_expense(test_expense)
        assert False
    except CustomError as error:
        assert str(error) == "The amount field must be positive and cannot be 0.00, please try again!"

def test_update_expense_success():
    result = expense_sao.update_expense(updated_expense)
    assert result.date != successful_expense.date and result.description != successful_expense.description and \
           result.amount != successful_expense.amount

def test_delete_expense_not_found():
    try:
        expense_sao.delete_expense(-37542792)
        assert False
    except CustomError as error:
        assert str(error) == "Expense not found, please try again!"

def test_delete_expense_id_not_integer():
    try:
        expense_sao.delete_expense('')
        assert False
    except CustomError as error:
        assert str(error) == "The expense ID field must be an integer, please try again!"

def test_delete_expense_success():
    result = expense_sao.delete_expense(current_expense_id)
    assert result

def test_delete_all_expenses_success():
    pass
