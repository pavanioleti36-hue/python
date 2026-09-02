sentence = "Python programming is enjoyable and educational"
words = sentence.split()
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print("Sentence:", sentence)
print("Words with more than 5 characters:", long_words)