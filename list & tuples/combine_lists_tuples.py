std= [("pavani", 98),
      ("sailu", 65),
      ("priya", 79),
      ("meghana", 37),
      ("manasa", 92),
      ("gayatri", 74)]
print("Students who got grater than 75 marks: ")
print("~"*40)
for n , m in std:
    if m > 75:
        print("*name :",n, " *marks : ",m )