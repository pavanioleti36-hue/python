class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print("Employee ID: " + str(self.emp_id))
        print("Name: " + self.name)
        print("Department: " + self.department)
        print("Salary: " + str(self.salary))


emp1 = Employee(101, "Rahul", "IT", 55000)
emp2 = Employee(102, "Priya", "HR", 65000)
emp3 = Employee(103, "Arjun", "Finance", 75000)

emp1.display_info()
print()
emp2.display_info()
print()
emp3.display_info()
