class InvalidSalaryError(Exception):
    pass
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        try:
            if self.salary < 0:
                raise InvalidSalaryError("Salary cannot be negative")
            print(self.name, self.salary)
        except InvalidSalaryError as e:
            print(e)
employee = Employee("Anu", -5000)
employee.display()