sentence = "pavani is a very good girl & she is very talented"
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word frequencies:")
for w, count in freq.items():
    print(w + " - " + str(count))