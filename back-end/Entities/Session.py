class Session:

    def __init__(self, session_id: int, user_id: int, expires: datetime):
        self.session_id = session_id
        self.user_id = user_id
        self.expires = expires

    def convert_to_dictionary(self):
        return {
            'sessionId': self.session_id,
            'userId': self.user_id,
            'expires': self.expires
        }
