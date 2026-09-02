courses = "C,DS,Python,Java,sql"
result = courses.split(",")
print(result)

sntce = "Pavani is a good girl"
words = sntce.split()
print(words)

text = "Python-Java-Data Science"
print(text.rsplit("-", 1))

msg = """Python
Java
Data Science"""
print(msg.splitlines())