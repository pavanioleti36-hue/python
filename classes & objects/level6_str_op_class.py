class StringOperations:
    def __init__(self, text):
        self.text = text

    def reverse_string(self):
        return self.text[::-1]

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for ch in self.text:
            if ch in vowels:
                count += 1
        return count

    def is_palindrome(self):
        return self.text == self.text[::-1]


# Example usage
s1 = StringOperations("madam")
s2 = StringOperations("hello")

print("Original:", s1.text)
print("Reversed:", s1.reverse_string())
print("Vowel count:", str(s1.count_vowels()))
print("Is palindrome:", str(s1.is_palindrome()))

print("Original:", s2.text)
print("Reversed:", s2.reverse_string())
print("Vowel count:", str(s2.count_vowels()))
print("Is palindrome:", str(s2.is_palindrome()))
