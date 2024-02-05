class Courier:
    def __init__(self, login, password, first_name):
        self.login = login
        self.password = password
        self.first_name = first_name

    def to_dict(self):
        return {
            'login': self.login,
            'password': self.password,
            'firstName': self.first_name
        }
