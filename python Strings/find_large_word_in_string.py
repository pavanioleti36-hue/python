sentence = input("Enter a sentence: ")
words = sentence.split()
large= ""
for word in words:
    if len(word) > len(large):
        large = word
print("Largest word:", large)