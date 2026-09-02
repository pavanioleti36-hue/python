text = "pavani#16 my pinno is 24255-CM-169"
numbers = ""
result = []
for ch in text:
    if ch.isdigit():
        numbers += ch
    else:
        if numbers != "":
            result.append(numbers)
            numbers = ""
if numbers != "":
    result.append(numbers)
print("Original string:", text)
print("Extracted numbers:", result)