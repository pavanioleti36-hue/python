emp_salary= int(input("Enter employee salary: "))
percentage_inc= int(input("Enter percentage increment: "))
new_salary= emp_salary + (emp_salary * percentage_inc / 100)
print("New salary =", new_salary)