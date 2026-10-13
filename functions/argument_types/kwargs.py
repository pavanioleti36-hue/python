def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
employee(name="Ravi", age=25, salary=30000, department="IT")