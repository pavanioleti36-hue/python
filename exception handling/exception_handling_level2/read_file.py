try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
finally:
    print("File operation completed")