from abc import ABC, abstractmethod

class HospitalEmployee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def work(self):
        pass

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)

class Doctor(HospitalEmployee):
    def work(self):
        print("Doctor treats patients")

class Nurse(HospitalEmployee):
    def work(self):
        print("Nurse takes care of patients")

class Pharmacist(HospitalEmployee):
    def work(self):
        print("Pharmacist provides medicines")

employees = [
    Doctor("Dr. Kumar", "D101"),
    Nurse("Anitha", "N101"),
    Pharmacist("Rahul", "P101")
]

for employee in employees:
    employee.display_details()
    employee.work()
    print()