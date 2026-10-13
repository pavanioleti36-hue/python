class InvalidTransactionError(Exception):
    pass
try:
    amount = float(input("Enter transaction amount: "))
    if amount <= 0:
        raise InvalidTransactionError("Transaction amount must be positive")
    print("Transaction successful")
except InvalidTransactionError as e:
    print(e)