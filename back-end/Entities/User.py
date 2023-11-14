class User:

    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, password: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def convert_to_dictionary_full(self):
        return {
            'userId': self.user_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'password': self.password
        }

    def convert_to_dictionary(self):
        return {
            'userId': self.user_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }
