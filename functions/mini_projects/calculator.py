def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"
def modulus(a, b):
    return a % b if b != 0 else "Cannot divide by zero"
while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Exit")
    choice = input("Enter choice: ")
    if choice == "6":
        break
    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operations = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": modulus}
        print("Result:", operations[choice](a, b))
    else:
        print("Invalid choice")