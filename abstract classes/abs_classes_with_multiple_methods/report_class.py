from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report Generated")

    def export(self):
        print("PDF Report Exported")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report Generated")

    def export(self):
        print("Excel Report Exported")

p = PDFReport()
e = ExcelReport()
p.generate()
p.export()
e.generate()
e.export()