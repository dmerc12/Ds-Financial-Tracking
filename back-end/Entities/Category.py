class Category:
    def __init__(self, category_id: int, category_name: str):
        self.category_id = category_id
        self.category_name = category_name

    def convert_to_dictionary(self):
        return {
            'categoryId': self.category_id,
            'categoryName': self.category_name
        }