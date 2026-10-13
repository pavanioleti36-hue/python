def is_positive(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
print(is_positive(-5))