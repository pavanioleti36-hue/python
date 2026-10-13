connection = None
try:
    connection = "Database Connection"
    print("Database connected")
except Exception:
    print("Connection failed")
finally:
    if connection:
        print("Database connection closed")