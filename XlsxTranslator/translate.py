"""bring it all together"""

from XlsxTranslator.readData import ReadData
from XlsxTranslator.translateCells import TranslateCells
import time


class Translate:

    def __init__(self, max_column=None):
        self.data = ReadData()
        if max_column is None:
            self.max_column = self.data.worksheet.max_column
        else:
            self.max_column = max_column

    def translateFile(self):
        originalStrings = self.data.readData(max_col=self.max_column)
        translateEngine = TranslateCells()
        translateEngine.acceptCookies()
        translatedStrings = []
        for col in originalStrings:
            translateEngine.inputText(col)
            time.sleep(5)
            translatedCol = translateEngine.outputText()
            print(translatedCol)
            time.sleep(5)
            translatedStrings.append(translatedCol)
            time.sleep(5)
            translateEngine.inputField.clear()

        return translatedStrings

    def populateColumns(self, translation):

        for i, col in enumerate(self.data.worksheet.iter_rows(min_col=1, max_col=self.max_column)):
            for j, cell in enumerate(col):
                cell.value = translation[j][i]


if __name__ == "__main__":
    tr = Translate()
    translatedList = tr.translateFile()
    tr.populateColumns(translatedList)
    tr.data.saveData()
