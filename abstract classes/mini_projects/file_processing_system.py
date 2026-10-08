from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class PDFHandler(FileHandler):
    def read(self):
        print("Reading PDF file:", self.filename)

    def write(self):
        print("Writing PDF file:", self.filename)

class CSVHandler(FileHandler):
    def read(self):
        print("Reading CSV file:", self.filename)

    def write(self):
        print("Writing CSV file:", self.filename)

class ExcelHandler(FileHandler):
    def read(self):
        print("Reading Excel file:", self.filename)

    def write(self):
        print("Writing Excel file:", self.filename)

class JSONHandler(FileHandler):
    def read(self):
        print("Reading JSON file:", self.filename)

    def write(self):
        print("Writing JSON file:", self.filename)

files = [
    PDFHandler("document.pdf"),
    CSVHandler("students.csv"),
    ExcelHandler("marks.xlsx"),
    JSONHandler("data.json")
]

for file in files:
    file.read()
    file.write()
    print()