class Employee:
    def calculate_salary(self):
        print("Employee salary is calculated")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary is calculated with bonus")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary is calculated with project allowance")
employee = Employee()
manager = Manager()
developer = Developer()
employee.calculate_salary()
manager.calculate_salary()
developer.calculate_salary()