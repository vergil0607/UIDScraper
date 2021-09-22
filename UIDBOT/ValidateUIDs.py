import openpyxl
from UIDBOT.Validation import Validation
import time


class ValidateUIDsFromExcel:

    def __init__(self):
        self.validation = Validation()
        # time.sleep(3)
        self.validation.acceptCookies()
        self.input = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\UID-Liste per 02.06.2021.xlsx"
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
        self.workbook.save(filename=r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\ValidatedUIDs.xlsx")


if __name__ == "__main__":
    UIDsWorkbook = ValidateUIDsFromExcel()
    UIDsWorkbook.validateUIDsInExcel(40)
    UIDsWorkbook.saveExcel()
    UIDsWorkbook.validation.Scraper.driver.close()
