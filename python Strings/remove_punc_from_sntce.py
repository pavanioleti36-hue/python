sentence = "hi pavani ! , how are you ?"
result = ""
for ch in sentence:
    if ch.isalnum() or ch.isspace():
        result += ch
print("Original sentence:", sentence)
print("Without punctuation:", result)