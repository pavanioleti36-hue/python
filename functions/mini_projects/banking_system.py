balance = 0
history = []
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        history.append(f"Deposited: {amount}")
    else:
        print("Enter a positive amount")
def withdraw(amount):
    global balance
    if amount <= 0:
        print("Enter a positive amount")
    elif amount <= balance:
        balance -= amount
        history.append(f"Withdrawn: {amount}")
    else:
        print("Insufficient balance")
def check_balance():
    print("Balance:", balance)
def transaction_history():
    print(history if history else "No transactions")
while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        deposit(float(input("Amount: ")))
    elif choice == "2":
        withdraw(float(input("Amount: ")))
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        break
    else:
        print("Invalid choice")