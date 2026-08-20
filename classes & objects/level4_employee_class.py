class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_salary(self):
        print("Employee Name: " + self.name)
        print("Employee ID: " + str(self.emp_id))
        print("Salary: " + str(self.salary))
        print("-" * 25)


emp1 = Employee("Ananya", 201, 50000)
emp2 = Employee("Rahul", 202, 60000)

emp1.display_salary()
emp2.display_salary()
