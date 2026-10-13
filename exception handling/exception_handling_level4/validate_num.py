num = int(input("Enter a number: "))
try:
    if num <= 0:
        raise ValueError("Number must be positive")
    print("Number:", num)
except ValueError as e:
    print(e)