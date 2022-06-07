class BankAccount:
    def __init__(self, account, int_rate, balance):
        self.account = account
        self.int_rate = int_rate
        self.balance = balance
        


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        else: 
            amount > self.balance
            self.balance = self.balance - 5
        return print("Insufficient funds: Charging a $5 fee")

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self, amount):
        self.balance = amount*0.10 + amount
        return self

Stef = BankAccount("Stef", 0.10, 100)   
Chris = BankAccount("Chris", 0.10, 1000)

Stef.deposit(100).deposit(100).deposit(100).withdraw(40).display_account_info()
Chris.deposit(100).deposit(1).withdraw(20).withdraw(16).withdraw(19.9).withdraw(40).display_account_info()

