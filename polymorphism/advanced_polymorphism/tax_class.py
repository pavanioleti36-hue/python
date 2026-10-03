class Tax:
    def calculate_tax(self, amount):
        pass
class GST(Tax):
    def calculate_tax(self, amount):
        return amount * 0.18
class IncomeTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.10
class ServiceTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.15
# Creating objects
gst = GST()
income = IncomeTax()
service = ServiceTax()
amount = 10000
print("GST:", gst.calculate_tax(amount))
print("Income Tax:", income.calculate_tax(amount))
print("Service Tax:", service.calculate_tax(amount))