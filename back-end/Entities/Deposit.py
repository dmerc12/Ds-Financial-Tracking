class Deposit:
    def __init__(self, deposit_id: int, category_id: int, date: str, description: str, amount: float):
        self.deposit_id = deposit_id
        self.category_id = category_id
        self.date = date
        self.description = description
        self.amount = amount

    def convert_to_dictionary(self):
        return {
            'depositId': self.deposit_id,
            'categoryId': self.category_id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount
        }
