class bankaccount:
    bank_name = "ABC Bank"

    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    def display_info(self):
        print("Account Holder: " + self.account_holder)
        print("Account Number: " + str(self.account_number))
        print("Bank Name: " + bankaccount.bank_name)
        print("-" * 25)
bankAccount1 = bankaccount("suma", 123456)
bankAccount2 = bankaccount("pravee", 987654)
bankAccount3 = bankaccount("Pavani", 456789)

bankAccount1.display_info()
bankAccount2.display_info()
bankAccount3.display_info()
