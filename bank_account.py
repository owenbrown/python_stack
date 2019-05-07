from decimal import Decimal


class BankAccount:
    def __init__(self, int_rate=0.0, balance=0.0):
        self.interest_rate = Decimal(int_rate)
        self.balance = Decimal(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount non-positive")
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal amount non-positive")
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.interest_rate / 100)
        return self


def test_bank_account():
    account = BankAccount(int_rate=10, balance=90)
    account.deposit(10)
    account.yield_interest()
    assert account.balance == 110
