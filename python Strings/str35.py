word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
if sorted(word1) == sorted(word2):
    print("Anagrams")
else:
    print("Not Anagrams")


#spaces replaced
text="pavani is a good girl"
res= text.replace(" ", "")   
print(res)

#remove extra spaces
msg="do     good     and be         good"
res= " ".join(msg.split())
print(res)