sentence = "pavani is a good girl"
words = sentence.split()
letter = "g"
result = []
for word in words:
    if word.lower().startswith(letter.lower()):
        result.append(word)
print("Original sentence:", sentence)
print("Words beginning with '" + letter + "':", result)