# User - base

# Member - Not pay bills and can do code
# Owner - Not pay bills and can do code
# Manager - Pay bills and can't do code

class User:

    def __init__(self, name, email):
        self._name = name
        self._email = email

    def work(self):
        raise NotImplementedError
