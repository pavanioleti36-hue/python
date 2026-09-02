text = "16pavani05oleti2009"
numbers = ""
for character in text:
    if character.isdigit():
        numbers += character
print(numbers)

#letters
text = "16pavani2009oleti05"
letters = ""
for character in text:
    if character.isalpha():
        letters += character
print(letters)

#special characters
text = "Python@123#Programming!"
special = ""
for character in text:
    if not character.isalnum() and not character.isspace():
        special += character    
print(special)    

#validate username
uname= input("enter username:-")
if uname.isalnum():
    print("valid username")
else:
    print("inavalid username")    