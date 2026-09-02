sentence = "pavani is a good girl"
words = sentence.split()
result = ""
for word in words:
    result += word[0].upper() + word[1:] + " "
print("Original sentence:", sentence)
print("Capitalized sentence:", result.strip())