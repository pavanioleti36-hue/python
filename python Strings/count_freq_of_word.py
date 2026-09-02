sentence = "pavani is a good girl"
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Sentence:", sentence)
print("Word frequencies:")
for key in freq:
    print(key, ":", freq[key])