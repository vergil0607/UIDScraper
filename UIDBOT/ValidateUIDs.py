import openpyxl
from UIDBOT.Validation import Validation
import time


class ValidateUIDsFromExcel:

    def __init__(self):
        self.validation = Validation()
        time.sleep(2)
        self.validation.acceptCookies()
        self.validation.close_windows()
        self.input = r"C:\Users\Wieser\Desktop\202106_Python\202106_Python\UIDBOT\ValidatedUIDsBU.xlsx"
        self.workbook = openpyxl.load_workbook(self.input)
        self.inputSheet = self.workbook['Table 1']
        self.inputSheet.insert_cols(6)
        self.inputSheet["F1"] = "Validation"

    def validateUIDsInExcel(self, maxUID=100):
        """loop through the rows of the Excel file"""
        for row in self.inputSheet.iter_rows(min_row=2, max_row=maxUID):
            print(row[0].value)
            if row[0].value is None:
                row[5].value = 'blank'
            elif self.validation.validateUID(row[0].value):
                row[5].value = 'valid'
            else:
                row[5].value = 'not valid'
            print(row[5].value)

    def saveExcel(self):
        """save update of Excel file"""
        self.workbook.save(filename="ValidatedUIDs.xlsx")


if __name__ == "__main__":
    UIDsWorkbook = ValidateUIDsFromExcel()
    UIDsWorkbook.validateUIDsInExcel(10)
    UIDsWorkbook.saveExcel()
    UIDsWorkbook.validation.Scraper.driver.close()
