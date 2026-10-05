class BillingService:
    def generate_bill(self, patient, amount):
        print("Patient:", patient)
        print("Bill Amount:", amount)


class Hospital:
    def __init__(self, name):
        self.name = name

    def create_bill(self, billing_service, patient, amount):
        billing_service.generate_bill(patient, amount)


hospital = Hospital("City Hospital")
billing = BillingService()

hospital.create_bill(billing, "Ravi", 5000)