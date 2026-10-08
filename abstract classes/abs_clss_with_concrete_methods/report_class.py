from abc import ABC, abstractmethod
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass
    def display_report_info(self):
        print("Report: Monthly Report")
class PDFReport(Report):
    def generate(self):
        print("PDF report generated")
class ExcelReport(Report):
    def generate(self):
        print("Excel report generated")
p = PDFReport()
e = ExcelReport()
p.generate()
p.display_report_info()
e.generate()
e.display_report_info()