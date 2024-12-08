# User - base

# Member - can see all members and all teams
# Owner - can see all members and all teams
# Manager - can't see all members and all teams

# On this case we have here a LSP issue, because a new behavior is expected from manager
# Looks like a duck, quacks like a duck but needs battery
class User:

    def __init__(self, name, email):
        self._name = name
        self._email = email

    @staticmethod
    def members():
        return ['user_1', 'user_2', 'team_1']
