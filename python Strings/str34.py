text = "python programming"
frequency = {}
for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1
print(frequency)


#words
sentence = "python is easy and python is powerful"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)

#duplicate
text = "programming"
result = ""
for character in text:
    if character not in result:
        result += character
print(result)

#repitation letter
val="pavpvani"
for char in val:
    if val.count(char)==1:
        print("first non-repeat character:-",char)
        break