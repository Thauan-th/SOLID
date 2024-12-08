from .user import User
from .developer import Developer


class Member(User, Developer):
    def __init__(self, name, email):
        super().__init__(name, email)
