class food:
    def prepare(self):
        print("food is prepared")
class pizza(food):
    def prepare(self):
        print("pizza is prepared")
class burger(food):
    def prepare(self):
        print("burger is prepared")
class biryani(food):
    def prepare(self):
        print("biryani is prepared")
p= pizza()
b= burger()
bir= biryani()
p.prepare()
b.prepare()
bir.prepare()