class  printer:
    def print(self):
        print("printing document")
class pdfprinter:
    def print(self):
        print("printing pdf document")
def print_c(obj):
    obj.print()
p= printer()
pdf= pdfprinter()
print_c(p)
print_c(pdf)                    