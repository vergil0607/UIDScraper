import openpyxl
from Validation import Validation
import time


class ValidateUIDsFromExcel:

    def __init__(self):
        self.validation = Validation()
        time.sleep(2)
        self.validation.acceptCookies()
        self.validation.close_windows()
        self.input = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use " \
                     r"Case\202106_Python\UIDBOT\ValidatedUIDs.xlsx"
        self.workbook = openpyxl.load_workbook(self.input)
        self.inputSheet = self.workbook['Table 1']
        self.numberofrows = len(self.inputSheet['A'])
        self.inputSheet.insert_cols(6)
        self.inputSheet["F1"] = "Validation"

    def validateUIDsInExcel(self, maxUID=100):
        """loop through the rows of the Excel file"""
        for j, row in enumerate(self.inputSheet.iter_rows(min_row=2, max_row=maxUID)):
            if j%10 == 0:
                print("{}/{} checked".format(j, self.numberofrows))
            self.tryScarping(row)

    def tryScarping(self, row, max_tries=3):
        for i in range(max_tries):
            time.sleep(4)
            try:
                print(row[0].value)
                if row[0].value is None:
                    row[5].value = 'blank'
                elif self.validation.validateUID(row[0].value):
                    row[5].value = 'valid'
                else:
                    row[5].value = 'not valid'
                print(row[5].value)
                break
            except:
                row[5].value = 'please check manually'
                continue

    def saveExcel(self):
        """save update of Excel file"""
        self.workbook.save(filename=r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use "
                                    r"Case\202106_Python\UIDBOT\ValidatedUIDs_Output.xlsx")

    def log(self, msg):
        with open('out.txt', 'a') as f:
            print(msg, '\n', file=f)


if __name__ == "__main__":
    UIDsWorkbook = ValidateUIDsFromExcel()
    UIDsWorkbook.validateUIDsInExcel(UIDsWorkbook.numberofrows)
    UIDsWorkbook.saveExcel()
    UIDsWorkbook.validation.Scraper.driver.close()
