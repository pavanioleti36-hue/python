balance = 5000
amount = int(input("Enter withdrawal amount: "))
try:
    if amount > balance:
        raise Exception("Insufficient balance")
    balance -= amount
    print("Remaining balance:", balance)
except Exception as e:
    print(e)