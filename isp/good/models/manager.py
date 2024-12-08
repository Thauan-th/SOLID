from .user import User


class Manager(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def work(self):
        return 'Paying the company bills...'
