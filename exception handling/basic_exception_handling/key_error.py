try:
    student = {"name": "Pavani", "age": 20}
    print(student["marks"])
except KeyError:
    print("Key not found")