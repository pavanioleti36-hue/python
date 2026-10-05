class Employee:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Employee:", self.name)
class Department:
    def __init__(self):
        self.employees = [
            Employee("Rahul"),
            Employee("Priya"),
            Employee("Kiran")
        ]
    def show_employees(self):
        for employee in self.employees:
            employee.display()
department = Department()
department.show_employees()