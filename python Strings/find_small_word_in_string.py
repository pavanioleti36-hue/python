str =" pavani is good girl"
words = str.split()
small = words[0]

for word in words:
    if len(word) < len(small):
        small = word
print("smallest word:", small)