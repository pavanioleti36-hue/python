text = input("Enter a string: ")
unique = True
for ch in text:
    if text.count(ch) > 1:
        unique = False
        break
if unique:
    print("The string contains only unique characters")
else:
    print("The string does not contain only unique characters")