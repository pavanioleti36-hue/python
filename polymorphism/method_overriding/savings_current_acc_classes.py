class bankacc:
    def calculate_intrest(self):
        print("bankacc balance is calculated")
class savingsacc(bankacc):
    def calculate_intrest(self):
        print("savings account balance is calculated")
class currentacc(bankacc):
    def calculate_intrest(self):
        print("current account balance is calculated")
s = savingsacc()
c = currentacc()
s.calculate_intrest()
c.calculate_intrest()