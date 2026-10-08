from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 50000

e = Manager("Pavani", 101)
print(e.name, e.employee_id, e.calculate_salary())