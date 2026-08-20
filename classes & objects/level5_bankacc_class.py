class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def display_info(self):
        print("Account Holder: " + self.account_holder)
        print("Account Number: " + self.account_number)
        print("Balance: " + str(self.balance))


account1 = BankAccount("Rahul", "ACC12345", 5000)
account2 = BankAccount("Priya", "ACC67890", 10000)
account3 = BankAccount("Arjun", "ACC54321", 7500)

account1.display_info()
print()
account2.display_info()
print()
account3.display_info()
