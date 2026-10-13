def get_result():
    try:
        num = int(input("Enter a number: "))
        divisor = int(input("Enter divisor: "))
        values = [10, 20, 30]
        index = int(input("Enter list index: "))
        print("Division:", num / divisor)
        print("Element:", values[index])
    except ValueError:
        print("Please enter valid integers")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except IndexError:
        print("Index is out of range")
get_result()