class Expense:
    def __init__(self, expense_id: int, category_id: int, date: str, description: str, amount: float):
        self.expense_id = expense_id
        self.category_id = category_id
        self.date = date
        self.description = description
        self.amount = amount

    def convert_to_dictionary(self):
        return {
            'expenseId': self.expense_id,
            'categoryId': self.category_id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount
        }
