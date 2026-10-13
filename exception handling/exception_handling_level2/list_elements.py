numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])
except ValueError:
    print("Please enter a valid index")
except IndexError:
    print("Invalid index")