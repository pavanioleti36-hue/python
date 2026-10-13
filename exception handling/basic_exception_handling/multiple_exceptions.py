try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ValueError:
    print("Invalid numeric input")
except ZeroDivisionError:
    print("Cannot divide by zero")