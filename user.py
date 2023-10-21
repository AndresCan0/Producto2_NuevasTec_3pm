from db_connection import DBConnection
        
class User:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self._password = password

    def login(self):
        # Logic to validate username and password
        print("User logged in successfully")

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
