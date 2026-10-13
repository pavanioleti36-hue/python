def largest(*args):
    if not args:
        return "No numbers provided"
    result = args[0]
    for n in args:
        if n > result:
            result = n
    return result
print(largest(10, 50, 30, 80, 20))