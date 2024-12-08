from .user import User


class Owner(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    @staticmethod
    def members():
        return ['user_1', 'user_2', 'team_1']
