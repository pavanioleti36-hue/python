class HospitalEmployee:
    def work(self):
        print("Employee is working")
class Doctor(HospitalEmployee):
    def treat(self):
        print("Doctor treats patient")
class Nurse(HospitalEmployee):
    def care(self):
        print("Nurse cares for patient")
class Patient:
    def __init__(self,name):
        self.name=name
class BillingService:
    def bill(self,amount):
        print("Bill:",amount)
class Hospital:
    def __init__(self):
        self.doctors=[Doctor()]
        self.nurses=[Nurse()]
        self.patients=[Patient("Pavani")]
    def generate_bill(self,service,amount):
        service.bill(amount)
hospital=Hospital()
hospital.doctors[0].treat()
hospital.generate_bill(BillingService(),5000)