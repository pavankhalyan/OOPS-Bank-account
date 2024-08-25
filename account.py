class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"\nAccount '{self.name}' created. Balance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Accepted")
        self.get_balance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit Accepted")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdrawal Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete! \n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. {error}')

Pavan = SavingsAcct(1000, "Pavan")
Rakesh = SavingsAcct(2000, "Rakesh")

Pavan.get_balance()
Rakesh.get_balance()

Rakesh.deposit(500)
Pavan.withdraw(100)
Pavan.transfer(200, Rakesh)

Danuja = InterestRewardAcct(100, "Danuja")
Danuja.get_balance()
Danuja.deposit(100)
