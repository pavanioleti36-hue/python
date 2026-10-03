from abc import ABC, abstractmethod
class file_process(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self, data):
        pass
class TextFile(file_process):
    def read(self):
        print("Reading from Text File")
    def write(self, data):
        print("Writing", data, "to Text File")
class CSVFile(file_process):
    def read(self):
        print("Reading from CSV File")
    def write(self, data):
        print("Writing", data, "to CSV File")
t= TextFile()
c = CSVFile()
t.read()
t.write("Hello World")
c.read()
c.write("Data")