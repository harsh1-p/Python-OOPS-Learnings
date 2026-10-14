#Bank Managment system 

class Banksystem:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance 

    def check_balance(self):
        print("Account Holder : ",self.name)
        print("Balane : ",self.balance)

    def withdraw(self,amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount >= self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawal succesful")
            print("Balance = ",self.balance)

    def deposit(self,amount):
        if amount > 0:
            print("Amount added Succesfully ")
            self.balance = self.balance + amount
            print("Balance = ",self.balance)
        else:
            print('Enter Valid amount')

name = input("Enter Name : ")
balance = int(input("Emter your intial balance : "))

acc = Banksystem(name,balance)

while True:
    print("----------MENU----------")
    print("1.Check Balance")
    print("2.Deposit Amount")
    print("3.Withdraw Amount")
    print("4.EXIT")

    choice = int(input("Enter you choice : "))

    if choice == 1:
        acc.check_balance()

    elif choice == 2:
        amount = int(input("Enter Amount : "))
        acc.deposit(amount)

    elif choice == 3:
        amount =  amount = int(input("Enter Amount : "))
        acc.withdraw(amount)

    elif choice == 4:
        print("THANK YOU!")
        break

    else:
        print("Enter correct Menu 1,2,3 or 4.")


