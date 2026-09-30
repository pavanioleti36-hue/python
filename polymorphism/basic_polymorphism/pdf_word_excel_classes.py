class pdf:
    def open(self):
        print("PDF file opened")
class word:
    def open(self):
        print("Word file opened")
class excel:
    def open(self):
        print("Excel file opened")
p= pdf()
w= word()
e= excel()
p.open()
w.open()
e.open()                        