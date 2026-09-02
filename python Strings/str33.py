#digits
text = input("Enter text: ")
count = 0
for character in text:
         if character.isdigit():
              count += 1
print("Digit Count:", count)

#spaces
text = input("Enter sentence: ")
count = 0
for character in text:
     if character == " ":
        count += 1
print("Space Count:", count)


#upper & lower 
text = input("Enter text: ")
upper_count = 0
lower_count = 0
for character in text:
    if character.isupper():
        upper_count += 1
    elif character.islower():
          lower_count += 1
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)