class InsufficientStockError(Exception):
    pass
try:
    stock = 10
    quantity = int(input("Enter quantity: "))
    if quantity <= 0 or quantity > stock:
        raise InsufficientStockError("Invalid quantity or insufficient stock")
    stock -= quantity
    print("Remaining stock:", stock)
except InsufficientStockError as e:
    print(e)