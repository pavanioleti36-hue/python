dictionary = {
    "Python": "A high-level programming language.",
    "Algorithm": "A step-by-step procedure to solve a problem.",
    "Database": "An organized collection of data.",
    "Compiler": "A program that translates code into machine language.",
    "Variable": "A storage location identified by a name."
}
word = input("Enter a word: ")

if word in dictionary:
    print(word + " - " + dictionary[word])
else:
    print("Sorry, the word is not in the dictionary.")