class Bank:
    def __init__(self,name,balance):
        self.name = name

        #Private attribute
        self.__balance = balance

        #getter
    def get_balance(self):
        print(f"Current Balance : {self.__balance}")

    def deposit(self,amount):
        self.__balance += amount
        print(f"Amount Deposited\nCurrent Balance {self.__balance}\n")

    def withdraw(self,withdraw):
        self.__balance -= withdraw
        if withdraw > self.__balance:
            print("Enter Valid Amount")
        else:
            print(f"Amount Withdrawn\nCurrent Balance {self.__balance}")

obj = Bank("Harsh",1000)
obj.deposit(1000)
obj.balance = 100000000
obj.withdraw(1000)

obj.get_balance()

        