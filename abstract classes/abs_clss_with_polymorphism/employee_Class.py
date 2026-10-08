from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary: 50000")

class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: 40000")

class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary: 35000")

employees = [Manager(), Developer(), Tester()]

for employee in employees:
    employee.calculate_salary()