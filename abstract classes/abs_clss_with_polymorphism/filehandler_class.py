from abc import ABC, abstractmethod
class filehandler(ABC):
    def write(self):
        pass
class pdffile(filehandler):
    def write(self):
        print("the pdf file is written")
class wordfile(filehandler):
    def write(self):
        print("the word file is written")
files= [pdffile(), wordfile()]
for file in files:
    file.write()