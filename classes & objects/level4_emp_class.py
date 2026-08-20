class Employee:
    def __init__(self, emp_id, name, department, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def display_info(self):
        print("ID: " + str(self.emp_id) + "\n Name: " + self.name + " \n Department: " + self.department + "\n Monthly Salary: " + str(self.monthly_salary) + " \n Annual Salary: " + str(self.annual_salary()))


emp1 = Employee(101, "Rahul", "IT", 55000)
emp2 = Employee(102, "Priya", "HR", 65000)
emp3 = Employee(103, "Arjun", "Finance", 75000)

emp1.display_info()
emp2.display_info()
emp3.display_info()
