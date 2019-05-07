class User(object):
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def make_deposit(self, amount) -> 'User':
        if amount <= 0:
            raise ValueError("negative deposit amount")

        self.balance += amount
        return self

    def make_withdrawal(self, amount) -> 'User':
        if amount <= 0:
            raise ValueError("non-positive withdrawal amount")
        if amount > self.balance:
            raise ValueError("Tried to remove more than balance")
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self

    def transfer_money(self, other_user, amount) -> bool:
        if amount < 0:
            raise ValueError("transfers must be positive")
        else:
            self.make_withdrawal(amount)
            other_user.balance += amount
            return self


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

guido = User(1)
guido.make_withdrawal(100).make_withdrawal(100).make_deposit(100).make_withdrawal(100).display_user_balance()
