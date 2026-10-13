numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index out of range")
except TypeError:
    print("Invalid index type")
except Exception:
    print("Something went wrong")