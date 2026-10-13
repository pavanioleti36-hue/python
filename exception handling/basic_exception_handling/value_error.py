try:
    value = "hello"
    number = int(value)
    print(number)
except ValueError:
    print("Invalid value for integer conversion")