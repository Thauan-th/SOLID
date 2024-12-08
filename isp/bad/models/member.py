from .user import User


class Member(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def pay_bills(self):
        pass
    
    def code(self):
        return '<code>'
