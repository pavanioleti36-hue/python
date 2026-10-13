age = int(input("Enter age: "))
try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")
except ValueError as e:
    print(e)