quantity = int(input("Enter quantity: "))
try:
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    print("Quantity:", quantity)
except ValueError as e:
    print(e)