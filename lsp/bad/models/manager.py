from .user import User


class Manager(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    # Manager should not have this permission, and it comes from the `super`
    # Incorrect abstraction because a new behavior shows up
    @staticmethod
    def members():
        raise Exception('Manger can not perform this action!')
