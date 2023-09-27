from datetime import datetime, timedelta

from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from Entities.Expense import Expense

expense_dao = ExpenseDALImplementation()
test_expense = Expense(0, 1, str(datetime.now()), 'test description', 25.00)
current_expense_id = 1
updated_expense = Expense(current_expense_id, test_expense.category_id,
                          str(datetime.now() - timedelta(hours=2, minutes=17, seconds=43)), 'updated', 50.00)

def test_create_expense_success():
    result = expense_dao.create_expense(test_expense)
    assert result.expense_id != 0

def test_get_all_expenses_success():
    result = expense_dao.get_all_expenses()
    assert len(result) > 0

def test_update_expense_success():
    result = expense_dao.update_expense(updated_expense)
    assert result.date != test_expense.date and result.description != test_expense.description and \
           result.amount != test_expense.amount

def test_delete_expense_success():
    result = expense_dao.delete_expense(current_expense_id)
    assert result
