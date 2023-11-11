from datetime import date


class Expense:
    def __init__(self, expense_id: int, user_id: int, category_id: int, expense_date: date, description: str, amount: float):
        self.expense_id = expense_id
        self.user_id = user_id
        self.category_id = category_id
        self.date = expense_date
        self.description = description
        self.amount = amount

    def convert_to_dictionary(self):
        return {
            'expenseId': self.expense_id,
            'userId': self.user_id,
            'categoryId': self.category_id,
            'date': self.date.strftime("%%%Y-%%m-%%d"),
            'description': self.description,
            'amount': self.amount
        }
