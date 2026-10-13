def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"
def show_menu():
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == "5":
        print("Program exited")
        break
    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operations = {"1": add, "2": subtract, "3": multiply, "4": divide}
        print("Result:", operations[choice](a, b))
    else:
        print("Invalid choice")