text = input("Enter a word: ")
if text == text[::-1]:
     print("Palindrome")
else:
     print("not a palindrome") 


text = input("Enter a word: ").lower()
if text == text[::-1]:
     print("Palindrome")
else:
     print("not a palindrome")     