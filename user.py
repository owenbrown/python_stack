class User(object):
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def make_withdrawal(self, amount) -> bool:

        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def display_user_balance(self):
        print(self.balance)

    def transfer_money(self, other_user, amount) -> bool:
        if amount < 0:
            return False
        else:
            other_user.balance += amount
            self.balance -= amount
            return True

