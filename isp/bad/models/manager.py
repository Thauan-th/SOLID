from .user import User


class Manager(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def pay_bills(self):
        return 'pay bills'
    
    def code(self):
        pass
