from .user import User
from .developer import Developer


class Owner(User, Developer):
    def __init__(self, name, email):
        super().__init__(name, email)

    @staticmethod
    def members():
        return ['user_1', 'user_2', 'team_1']
