class  excelreport:
    def generate(self):
        print("generating excel report")
class pdfreport:
    def generate(self):
        print("generating pdf report")
def obj_cls(obj):
    obj.generate()
excel= excelreport()
pdf= pdfreport()
obj_cls(excel)
obj_cls(pdf)                    