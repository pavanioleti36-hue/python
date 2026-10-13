try:
    file = open("numbers.txt", "r")
    for line in file:
        try:
            print(int(line.strip()))
        except ValueError:
            print("Invalid data:", line.strip())
    file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("File error")