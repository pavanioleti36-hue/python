try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter operator: ")
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        print(a / b)
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Invalid type")