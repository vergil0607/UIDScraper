import openpyxl
from Validation import Validation
import time
from datetime import datetime
import os
from parameters import Parameters


class ValidateUIDsFromExcel:

    def __init__(self):
        self.timestamp = datetime.now().strftime('%Y%m%d')
        self.validation = Validation()
        self.input = Parameters.filein
        self.workbook = openpyxl.load_workbook(self.input)
        self.inputSheet = self.workbook[Parameters.tabname]
        self.numberofrows = len(self.inputSheet['A'])
        self.inputSheet.insert_cols(Parameters.newcolix)
        self.inputSheet[Parameters.newcolumn] = "Validation"

    def validateUIDsInExcel(self, maxUID=100):
        """loop through the rows of the Excel file"""
        for j, row in enumerate(self.inputSheet.iter_rows(min_row=2, max_row=maxUID)):
            if j % 10 == 0:
                print(j)
            self.tryScarping(row)

    def tryScarping(self, row, max_tries=3):
        if row[0].value is None:
            row[Parameters.newcolix-1].value = 'blank'
        else:
            uid = row[0].value.strip()
            for i in range(max_tries):
                try:
                    self.log(uid)
                    if self.validation.makeRequest(uid):
                        row[Parameters.newcolix-1].value = 'valid'
                    else:
                        row[Parameters.newcolix-1].value = 'not valid'
                    self.log(row[Parameters.newcolix-1].value)
                    break
                except Exception as e:
                    print(e)
                    self.saveExcel()
                    time.sleep(3)
                    row[Parameters.newcolix-1].value = 'please check manually'
                    continue

    def saveExcel(self):
        """save update of Excel file"""
        self.workbook.save(filename=Parameters.fileout)

    def log(self, msg):
        with open(self.timestamp + '_log.txt', 'a') as f:
            print(msg)
            print(msg, file=f)


if __name__ == "__main__":
    UIDsWorkbook = ValidateUIDsFromExcel()
    if Parameters.check_all:
        UIDsWorkbook.validateUIDsInExcel(UIDsWorkbook.numberofrows)
    else:
        UIDsWorkbook.validateUIDsInExcel(Parameters.Limit)
    UIDsWorkbook.saveExcel()
    UIDsWorkbook.validation.Scraper.driver.close()
