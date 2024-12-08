from .user import User


class Manager(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    # Will not have the method anymore and the `super` will not bring the behavior
    # So this class is clean as possible
