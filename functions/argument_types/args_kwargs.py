def student(*args, **kwargs):
    print("Details:", args)
    print("Marks:", kwargs)
student("Ravi", 20, Maths=90, Science=85, English=88)