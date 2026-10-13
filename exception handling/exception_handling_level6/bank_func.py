def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient balance")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        balance -= amount
        print("Remaining balance:", balance)
    except ValueError as e:
        print(e)
withdraw(5000, 6000)