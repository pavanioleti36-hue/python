def average(*args):
    if not args:
        return "No numbers provided"
    return sum(args) / len(args)
print(average(10, 20, 30, 40, 50))