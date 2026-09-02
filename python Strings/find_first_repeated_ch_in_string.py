text = "pavbajji"
for i in range(len(text)):
    for j in range(i+1, len(text)):
        if text[i] == text[j]:
            print("First repeated character:", text[i])
            exit()
print("No repeated character found")