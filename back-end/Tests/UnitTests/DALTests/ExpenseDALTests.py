from datetime import datetime, timedelta

from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from Entities.Expense import Expense

expense_dao = ExpenseDALImplementation()
test_expense = Expense(0, -1, -1, datetime.now().date(), 'test description', 25.00)
current_expense_id = 1
updated_expense = Expense(current_expense_id, test_expense.user_id, test_expense.category_id,
                          datetime.now().date() - timedelta(days=5), 'updated', 50.00)

def test_create_expense_success():
    result = expense_dao.create_expense(test_expense)
    assert result.expense_id != 0

def test_get_expense_success():
    result = expense_dao.get_expense(current_expense_id)
    assert result is not None

def test_get_all_expenses_success():
    result = expense_dao.get_all_expenses(test_expense.user_id)
    assert len(result) > 0

def test_get_expenses_by_category_success():
    result = expense_dao.get_expenses_by_category(test_expense.category_id)
    assert len(result) > 0

def test_get_expenses_by_date_success():
    result = expense_dao.get_expenses_by_date(test_expense.date)
    assert len(result) > 0

def test_get_expenses_by_description_key_words_success():
    result = expense_dao.get_expenses_by_description_key_words(["test", "description"])
    assert len(result) > 0

def test_get_total_by_category_success():
    result = expense_dao.get_total_by_category(test_expense.category_id)
    assert result is not None

def test_get_total_by_month_success():
    result = expense_dao.get_total_by_month(test_expense.date.month, test_expense.date.year)
    assert result is not None

def test_get_total_by_year_success():
    result = expense_dao.get_total_by_year(test_expense.date.year)
    assert result is not None

def test_update_expense_success():
    result = expense_dao.update_expense(updated_expense)
    assert result

def test_delete_expense_success():
    result = expense_dao.delete_expense(current_expense_id)
    assert result

def test_delete_all_expenses_success():
    result = expense_dao.delete_all_expenses(-2)
    assert result
