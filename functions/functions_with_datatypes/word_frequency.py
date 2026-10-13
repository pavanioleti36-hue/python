def word_frequency(sentence):
    frequency = {}
    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
print(word_frequency("python is easy and python is useful"))