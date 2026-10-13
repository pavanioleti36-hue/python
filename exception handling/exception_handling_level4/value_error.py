num = int(input("Enter a number: "))
try:
    if num < 0:
        raise ValueError("Number cannot be negative")
    print("Number:", num)
except ValueError as e:
    print(e)