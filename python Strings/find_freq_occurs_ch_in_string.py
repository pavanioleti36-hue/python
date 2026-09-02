text = input("Enter a string: ")
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
max_char = max(freq, key=freq.get)
print("Most frequently occurring character:", max_char)
print("Frequency:", freq[max_char])