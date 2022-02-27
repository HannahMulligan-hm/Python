class BankAccount:
    def __init__(self, int_rate= 0.01, balance=0):
        self.rate = 0.01
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Account:", self.balance, "Interest Rate:", self.rate)
        return self
    def yield_interest(self):
        if self.balance > 0:
            temp = self.balance * self.rate
            self.balance += temp
        return self

savings = BankAccount(0.05,1000)
checking = BankAccount(0.01,100)

savings.deposit(100).deposit(900).deposit(200).withdraw(50).yield_interest().display_account_info()
checking.deposit(500).deposit(500).withdraw(60).withdraw(40).withdraw(30).withdraw(67).yield_interest().display_account_info()