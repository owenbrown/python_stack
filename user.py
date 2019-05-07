class User(object):
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def make_deposit(self, amount) -> bool:
        if amount <= 0:
            return False
        else:
            self.balance += amount
            return True

    def make_withdrawal(self, amount) -> bool:
        if amount <= 0:
            return False
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

larry = User(10)
curly = User(5)
moe = User(3)

larry.make_deposit(1)
larry.make_deposit(1)
larry.make_deposit(1)
larry.make_withdrawal(5)
larry.display_user_balance()

curly.make_deposit(5)
curly.make_deposit(5)
curly.make_withdrawal(3)
curly.make_withdrawal(3)
curly.display_user_balance()

moe.make_deposit(34)
moe.display_user_balance()

larry.transfer_money(moe, 2)
larry.display_user_balance()
moe.display_user_balance()