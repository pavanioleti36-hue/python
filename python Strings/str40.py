phone = "9121212343"
security="******"+ phone[-4:]
print(security)

#email masking
email = "ravi@example.com"
username, domain = email.split("@")
masked = username[0] + "***@" + domain
print(masked)

#formating
name="pavani"
course="cse"
print(f"student name:-{name}")
print(f"student course:-{course}")

#centering text
text="pavani"
print(text.center(30))

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
print(add(2,45))