try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Square:", num ** 2)