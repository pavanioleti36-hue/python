with open("newfile.txt", "r") as file:
        print(file.tell())
        file.read(11)
        print(file.tell())  