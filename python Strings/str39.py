sentence = input("Enter sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest Word:", longest)

#short word
sentence = input("Enter sentence: ")
words = sentence.split()
shortest = min(words, key=len)
print("Shortest Word:", shortest)

#count words in a sentence
stce= input("enter a sentence:-")
words= stce.split()
print("Total Words:", len(words))

#covert into title case
title = input("Enter course title: ")
print(title.title())

#slug
title = "Python Full Stack Development Course"
slug = title.lower().replace(" ", "-")
print(slug)