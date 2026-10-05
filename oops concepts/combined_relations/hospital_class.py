class Doctor:
    def __init__(self, name):
        self.name = name
class Patient:
    def __init__(self, name):
        self.name = name
class BillingService:
    def generate_bill(self, amount):
        print("Hospital Bill:", amount)
class Hospital:
    def __init__(self):
        self.doctors = [Doctor("Dr. Ravi"), Doctor("Dr. Anu")]
        self.patients = [Patient("Pavani"), Patient("Rahul")]
    def create_bill(self, billing_service, amount):
        billing_service.generate_bill(amount)
hospital = Hospital()
billing = BillingService()
hospital.create_bill(billing, 5000)