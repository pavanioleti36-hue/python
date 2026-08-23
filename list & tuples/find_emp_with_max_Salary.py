emp= [("bhaskar", "police", 40000),
      ("pavani", "engineer", 66000),
      ("srinivas", "manager", 52000),
      ("naresh", "artist", 50000)]
large= emp[0]
for x in emp:
    if x[2]> large[2]:
        large= x
print("this emp have highest salary : ")
print("name: ",large[0])
print("designation:",large[1])
print("salary:",large[2])