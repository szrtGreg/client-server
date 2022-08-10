

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role.upper()

    def __str__(self):
        return self.username

    def get_user_data(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
        }
