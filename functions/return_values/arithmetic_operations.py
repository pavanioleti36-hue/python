def operations(a, b):
    division = a / b if b != 0 else "Cannot divide by zero"
    return a + b, a - b, a * b, division
print(operations(10, 5))