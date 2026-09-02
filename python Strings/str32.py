#reverse string
text = "pavani"
reversed_text = ""
for character in text:
      reversed_text = character + reversed_text
print(reversed_text)

#vowels
char= input("enter a text:-")
vowels="aeiou"
count=0
for text in char:
      if text in vowels:
            count+=1
print("vowels count in text:-",count)            

#consonants
text = input("Enter text: ").lower()
vowels = "aeiou"
count = 0
for character in text:
      if character.isalpha() and character not in vowels:
             count += 1
print("Consonant Count:", count)