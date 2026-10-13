student = {"name": "Pavani", "age": 20, "course": "Python"}
try:
    key = input("Enter key: ")
    if not key:
        raise ValueError("Invalid input")
    print(student[key])
except ValueError as e:
    print(e)
except KeyError:
    print("Key not found")
except TypeError:
    print("Invalid key type")