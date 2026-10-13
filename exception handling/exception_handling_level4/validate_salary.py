salary = float(input("Enter salary: "))
try:
    if salary < 0:
        raise ValueError("Salary cannot be negative")
    print("Salary:", salary)
except ValueError as e:
    print(e)