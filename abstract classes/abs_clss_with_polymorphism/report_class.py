from abc import ABC, abstractmethod
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass
class PDFReport(Report):
    def generate(self):
        print("PDF Report Generated")
class ExcelReport(Report):
    def generate(self):
        print("Excel Report Generated")
class WordReport(Report):
    def generate(self):
        print("Word Report Generated")
reports = [PDFReport(), ExcelReport(), WordReport()]
for report in reports:
    report.generate()