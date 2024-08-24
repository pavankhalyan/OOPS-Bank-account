class BankAccount: 
    def __init__(self, initial_amount,acc_name): 
        self.balance = initial_amount 
        self.name = acc_name 
        print(f"\nAccount '{self.name}' created.Balance = ${self.balance}") 