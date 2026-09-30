class  androidphone:
    def call(self):
        print("android phone making a call ")
class iphone:
    def call(self):
        print("iphone making a call")
def obj_cls(obj):
    obj.call()
android= androidphone()
i= iphone()
obj_cls(android)
obj_cls(i)                    