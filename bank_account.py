'''QUESTION:-
Create a class BankAccount that:
Initializes with balance = 0.
Has methods:
deposit(amount) → add money.
withdraw(amount) → subtract money if balance is enough, else show "Insufficient Balance".
get_balance() → prints balance.'''

class BankAccount:
    balance=0
    
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited")
    def withdraw(self,amount):
        if amount>self.balance or self.balance<=0:
            print("Insufficient Balance")
            return
        self.balance-=amount;
        print(amount,"withdrawl sucessfully")
    def get_balance(self):
        print(self.balance)
    
#main body
p1=BankAccount()
p1.get_balance()
p1.deposit(5000)
p1.get_balance()
p1.withdraw(500)
p1.get_balance()
