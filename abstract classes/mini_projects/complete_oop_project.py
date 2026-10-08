from abc import ABC, abstractmethod

class Employee(ABC):
    company = "ABC Technologies"

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def work(self):
        pass

    def display_details(self):
        print("Company:", Employee.company)
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000

    def work(self):
        print(self.name, "manages the team")

class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000

    def work(self):
        print(self.name, "develops software")

class Tester(Employee):
    def calculate_salary(self):
        return self.salary + 3000

    def work(self):
        print(self.name, "tests software")

employees = [
    Manager("Ravi", "M101", 60000),
    Developer("Pavani", "D101", 50000),
    Tester("manoj", "T101", 60000)
]

for employee in employees:
    employee.display_details()
    employee.work()
    print("Final Salary:", employee.calculate_salary())
    print()