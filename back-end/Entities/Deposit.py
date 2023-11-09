from datetime import date


class Deposit:
    def __init__(self, deposit_id: int, category_id: int, deposit_date: date, description: str, amount: float):
        self.deposit_id = deposit_id
        self.category_id = category_id
        self.date = deposit_date
        self.description = description
        self.amount = amount

    def convert_to_dictionary(self):
        return {
            'depositId': self.deposit_id,
            'categoryId': self.category_id,
            'date': self.date.strftime("%Y-%m-%d"),
            'description': self.description,
            'amount': self.amount
        }
