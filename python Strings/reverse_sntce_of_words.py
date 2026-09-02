sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""
for word in words:
    reversed_word = ""
    for ch in word:
        reversed_word = ch + reversed_word
    result += reversed_word + " "
print("Sentence with each word reversed:", result.strip())     