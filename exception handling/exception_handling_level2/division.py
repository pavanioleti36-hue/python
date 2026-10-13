try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
else:
    print("Result:", result)