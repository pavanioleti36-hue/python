#left align
text = "Python"
print(text.ljust(20, "-"))

#right align
text = "Python"
print(text.rjust(20, "-"))

#zero fill
num="69"
print(num.zfill(16))

#email partition
email = "ravi@example.com"
result = email.partition("@")
print(result)

#right partition
path = "folder/subfolder/file.txt"
print(path.rpartition("/"))

#doc
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
print(add.__doc__)
print(add(5,45))