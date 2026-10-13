def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c:
        return b
    return c
print(smallest(10, 25, 15))