class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12


emp1 = Employee("Ananya", 50000)
emp2 = Employee("Rahul", 60000)

print(emp1.name + " annual salary: " + str(emp1.annual_salary()))
print(emp2.name + " annual salary: " + str(emp2.annual_salary()))

