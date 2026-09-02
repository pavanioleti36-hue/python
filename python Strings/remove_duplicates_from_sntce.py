sentence = "pavani is a very very good good girl good girl"
words = sentence.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

result = " ".join(unique_words)
print("Original sentence:", sentence)
print("Sentence without duplicate words:", result)