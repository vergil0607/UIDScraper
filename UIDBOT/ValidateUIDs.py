import openpyxl
from Validation import Validation
import time
from datetime import datetime
import os

PATH = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\202106_Python\UIDBOT"


class ValidateUIDsFromExcel:

    def __init__(self, headless):
        self.timestamp = datetime.now().strftime('%Y%m%d')
        self.validation = Validation(headless)
        self.validation.acceptCookies()
        self.validation.close_windows()
        self.input = os.path.join(PATH, "ValidatedUIDs.xlsx")
        self.workbook = openpyxl.load_workbook(self.input)
        self.inputSheet = self.workbook['Table 1']
        self.numberofrows = len(self.inputSheet['A'])
        self.inputSheet.insert_cols(6)
        self.inputSheet["F1"] = "Validation"

    def validateUIDsInExcel(self, maxUID=100):
        """loop through the rows of the Excel file"""
        for j, row in enumerate(self.inputSheet.iter_rows(min_row=2, max_row=maxUID)):
            if j % 10 == 0:
                self.log("{}/{} checked".format(j, self.numberofrows))
            self.tryScarping(row)

    def tryScarping(self, row, max_tries=3):
        for i in range(max_tries):
            time.sleep(4)
            try:
                self.log(row[0].value)
                if row[0].value is None:
                    row[5].value = 'blank'
                elif self.validation.validateUID(row[0].value):
                    row[5].value = 'valid'
                else:
                    row[5].value = 'not valid'
                self.log(row[5].value)
                break
            except:
                row[5].value = 'please check manually'
                continue

    def saveExcel(self):
        """save update of Excel file"""
        self.workbook.save(filename=os.path.join(PATH, "ValidatedUIDs_Output.xlsx"))

    def log(self, msg):
        with open('../logs/' + self.timestamp + '_log.txt', 'a') as f:
            print(msg)
            print(msg, file=f)


if __name__ == "__main__":
    UIDsWorkbook = ValidateUIDsFromExcel(headless=False)
    UIDsWorkbook.validateUIDsInExcel(100)  # UIDsWorkbook.numberofrows)
    UIDsWorkbook.saveExcel()
    UIDsWorkbook.validation.Scraper.driver.close()
