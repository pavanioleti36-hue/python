sentence = "pavani16 is a good girl"
words = sentence.split()
word_count = len(words)
char_count = len(sentence)
digit_count = 0
vowel_count = 0
space_count = 0
vowels = "aeiouAEIOU"
for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    if ch in vowels:
        vowel_count += 1
    if ch.isspace():
        space_count += 1
print("Sentence:", sentence)
print("Number of words:", word_count)
print("Number of characters:", char_count)
print("Number of digits:", digit_count)
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)