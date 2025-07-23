'''
Write a python program to create a class with name ‘Bank’. In Bank class take three instance variables acno, name and balance. Create a parameterized constructor to initialize instance variables. Now create following methods in Bank class:-
'''
class Bank:
    def __init__(self, acno, name, balance):
        self.acno = acno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = balance + amount
        print("Deposited" ,amount, "in" ,"account" ,self.acno, "New balance is", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = balance - amount
            print("Withdrew", amount , "from account", self.acno , "New balance is",self.balance)

    def enquiry(self):
        print("Account Number:",self.acno)
        print("Account Holder:",self.name)
        print("Balance:",self.balance)

#  Bank object
acno = input("Enter account number: ")
name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

bank = Bank(acno, name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Enquiry")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        bank.deposit(amount)
    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        bank.withdraw(amount)
    elif choice == "3":
        bank.enquiry()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
