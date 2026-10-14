"""Practice Question: Bank Account
Task: Create a class called BankAccount that displays a customer's name and account balance.
Your program should:
1. Create a class named BankAccount.
2. Create a method named display() to print the customer's name and balance.
3. Create two objects: a1 and a2.
4. Display the details of both accounts."""

class Bankaccount:

    def display(self,name,balance):
        print(f"The balance of {name} is {balance}")

a1 = Bankaccount()
a1.display("Rahul",50000)

a2 = Bankaccount()
a2.display("Harsh",10000000000)

