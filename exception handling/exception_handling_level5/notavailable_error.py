class BookNotAvailableError(Exception):
    pass
try:
    available = False
    if not available:
        raise BookNotAvailableError("Book is not available")
    print("Book issued successfully")
except BookNotAvailableError as e:
    print(e)