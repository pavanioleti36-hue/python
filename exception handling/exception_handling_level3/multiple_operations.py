try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Addition:", a + b)
    print("Division:", a / b)
    print("List value:", numbers[index])
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")
except TypeError:
    print("Invalid type")