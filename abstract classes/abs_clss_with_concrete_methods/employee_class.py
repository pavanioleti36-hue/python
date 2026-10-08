from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_company(self):
        print("Company: ABC Company")
class Manager(Employee):
    def calculate_salary(self):
        print("Salary: 50000")
class Developer(Employee):
    def calculate_salary(self):
        print("Salary: 40000")
m = Manager()
d = Developer()
m.calculate_salary()
m.display_company()
d.calculate_salary()
d.display_company()