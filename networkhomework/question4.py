class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(
                f"An amount has been deposited: ${amount}. The total amount in the account is ${self.balance}")
        else:
            print("It is impossible for the deposit to be a negative number, please contact the customer service center")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(
                f"An amount has been withdrawn: ${amount}. The total amount in the account is ${self.balance}")
        else:
            print(
                f"Wrong entry, or the total value of the account is less than the amount to be withdrawn. The total value of the account is: ${self.balance}")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(
            f"Interest was applied to the amount amounting to: ${interest}")
        print(f"The total amount after applying interest is: ${self.balance}")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}, Interest Rate: {self.interest_rate}%"


account = BankAccount("2825", "Almekdad Bassam Msallam")
account.deposit(1000)
account.withdraw(500)

print("\n, Example of instance of savingaccount\n PLEASE ENTER ACCOUNT NUMBER: ")
x = input()
print("PLEASE ENTER A name of accout number: ")
y = input()
print("PLEASE ENTER INTERSET %: ")
z = int(input())
print("PLEASE ENTER DEPOSIT: ")
zz = int(input())
savings_account = SavingsAccount(x, y, z)
savings_account.deposit(zz)
savings_account.apply_interest()
print(savings_account)
print(f"Thank you {y} ")
