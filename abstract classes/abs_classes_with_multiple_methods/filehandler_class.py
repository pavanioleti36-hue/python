from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class PDFFile(FileHandler):
    def read(self):
        print("Reading PDF")

    def write(self):
        print("Writing PDF")

class CSVFile(FileHandler):
    def read(self):
        print("Reading CSV")

    def write(self):
        print("Writing CSV")

class ExcelFile(FileHandler):
    def read(self):
        print("Reading Excel")

    def write(self):
        print("Writing Excel")

p = PDFFile()
c = CSVFile()
e = ExcelFile()
p.read()
p.write()
c.read()
c.write()
e.read()
e.write()