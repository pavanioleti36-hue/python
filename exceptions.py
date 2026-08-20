try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
except ValueError as e:
    print("Invalid input:", e)