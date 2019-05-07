from decimal import Decimal


class BankAccount:
    def __init__(self, int_rate=0.0, balance=0.0, name="My Account"):
        self.interest_rate = Decimal(int_rate)
        self.balance = Decimal(balance)
        self.name = name

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
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.interest_rate / 100)
        return self


def test_bank_account():
    account = BankAccount(int_rate=10, balance=90)
    account.deposit(3).deposit(3).deposit(5).withdraw(1).yield_interest().display_account_info()
    assert account.balance == 110

    account_2 = BankAccount().deposit(3).deposit(1).withdraw(1).withdraw(2).withdraw(3).withdraw(4). \
        display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate=0.02, balance=0)]  # added this line

    @property
    def account(self):
        return self.accounts[0]

    def make_deposit(self, amount):
        if len(self.accounts) == 1:
            self.account.deposit(amount)
        else:
            for account in self.accounts:
                print("{:<30}${:>30}".format(account.name, account.balance))
            index = False
            while index is False:
                selector = input("Please type the name of the account you'd like to deposit to:\n")
                try:
                    index = [account.name for account in self.accounts].index(selector)
                except ValueError:
                    print("try again")

            return self.accounts[index].deposit(amount)

    def make_withdrawal(self, amount):
        self.accounts[0].withdraw(amount)


if __name__ == '__main__':
    samuel = User(name='Samuel L Jackson', email="vincent@vega.com")
    samuel.make_deposit(55)
    samuel.accounts.append(BankAccount(int_rate=7.8, balance=77, name="Hector"))
    samuel.make_deposit(33)
