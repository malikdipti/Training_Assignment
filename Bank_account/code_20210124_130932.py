# Case Studies:
# Define a class to represent a Bank account including the following members:
# Data Variables: Name of the Depositor, Account Number, Type of the Account,
#                 Balance amount in the account
# Data Methods: Assign initial value to deposit amount, to withdraw an amount
#               after checking the balance to display name and balance.


class Bankaccount:
    def details(self):
        self.balance = 0.0
        self.name = "Diptiranjan"
        self.acno = 452387690512
        self.actype = "saving"
        print("Account Holder Name:", self.name)
        print("Acconunt Number:", self.acno)
        print("Account Type:", self.actype)

    def deposit(self):
        amount = float(input("Enter amount to be deposited:"))
        if amount <= 0:
            print("invalid amount")
        else:
            self.balance += amount
            print("Amount Deposited :", amount)

    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn:"))

        if amount > 10000:
            print("beyond the excess limit")

        elif self.balance >= amount:
            self.balance -= amount
            print("You withdraw:", amount)
        else:
            print("insufficient balance:")

    def display(self):
        print("Available Balance:", self.balance)


s = Bankaccount()
s.details()
s.deposit()
s.withdraw()
s.display()
