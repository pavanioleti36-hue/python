from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    def calculate_salary(self):
        return self.salary  
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
f= FullTimeEmployee(50000)
p = PartTimeEmployee(20, 80)
print("Full Time Employee Salary:", f.calculate_salary())
print("Part Time Employee Salary:", p.calculate_salary())