def access_element(items, index):
    try:
        print("Element:", items[index])
    except IndexError:
        print("Index is out of range")
access_element([10, 20, 30], 5)