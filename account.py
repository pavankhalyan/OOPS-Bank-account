class BalanceException(Exception):
    pass

class BankAccount: 
    def __init__(self, initial_amount,acc_name): 
        self.balance = initial_amount 
        self.name = acc_name 
        print(f"\nAccount '{self.name}' created.Balance = ${self.balance:.2f}") 

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}") 

    def deposit(self, amount):
        self.balance += amount 
        print("\nDeposit Accepted")
        self.get_balance() 

    def viable_transaction(self,amount): 
        if self.balance >= amount: 
            return
        else: 
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}") 
        
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdrawal Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}')