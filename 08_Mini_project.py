class ATM:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def check_balance(self):
        print("Name : ",self.owner)
        print("Balance : ",self.balance)

    def deposit(self,amount):
        if amount <= 0:
            print("Enter valid amount")
        else:
            self.balance = amount + self.balance
            print("New Balance : ",self.balance)
            print("Amount deposited succesfully.")

    def withdraw(self,withdrawing):
        if self.balance <= 0:
            print("Money cannot be debited.")
        elif withdrawing <= 0:
            print("Enter valid amount.")
        else:
            self.balance = self.balance - withdrawing
            print("Balacne after withdraw : ",self.balance)
            print('Withdrawal Succesfull.')

atm1 = ATM("Rahul",5000)
atm1.check_balance()
atm1.deposit(5000)
atm1.withdraw(1000)



        

