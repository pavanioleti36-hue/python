class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def calculate_salary(self, working_days):
        return self.daily_salary * working_days


emp1 = Employee("Ananya", 1000)
emp2 = Employee("Rahul", 1200)

print(emp1.name + " salary for 25 days: " + str(emp1.calculate_salary(25)))
print(emp2.name + " salary for 20 days: " + str(emp2.calculate_salary(20)))
