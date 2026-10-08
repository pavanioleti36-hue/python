from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)

class Manager(Employee):
    def calculate_salary(self):
        return 60000

class Developer(Employee):
    def calculate_salary(self):
        return 50000

class Tester(Employee):
    def calculate_salary(self):
        return 40000

employees = [
    Manager("Ravi", "M101"),
    Developer("Pavani", "D101"),
    Tester("manoj", "T101")
]

for employee in employees:
    employee.display_details()
    print("Salary:", employee.calculate_salary())
    print()