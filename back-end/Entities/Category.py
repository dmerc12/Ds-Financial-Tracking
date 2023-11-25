class Category:
    def __init__(self, category_id: int, user_id: int, group: str, category_name: str):
        self.category_id = category_id
        self.user_id = user_id
        self.group = group
        self.category_name = category_name

    def convert_to_dictionary(self):
        return {
            'categoryId': self.category_id,
            'userId': self.user_id,
            'group': self.group,
            'categoryName': self.category_name
        }
