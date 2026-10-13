student = {"name": "Pavani", "age": 20, "course": "Python"}
try:
    key = input("Enter key: ")
    print("Value:", student[key])
except KeyError:
    print("Key not found")