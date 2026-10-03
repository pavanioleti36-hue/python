class SavingsAccount:
    def calculate_interest(self, amount):
        return amount * 0.06
class CurrentAccount:
    def calculate_interest(self, amount):
        return amount * 0.02
class FixedDeposit:
    def calculate_interest(self, amount):
        return amount * 0.08
accounts = [SavingsAccount(), CurrentAccount(), FixedDeposit()]
amount = 100000
for account in accounts:
    print("Interest:", account.calculate_interest(amount))