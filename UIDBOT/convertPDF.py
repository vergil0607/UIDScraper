import pandas as pd
import pdfplumber


class TagUIDPdfConverter:

    def __init__(self, file: str):
        self.pdffile = file
        self.table = pd.DataFrame(columns=['Umsatzsteuer-Id.Nr', 'Lnd', 'Name 1', 'Debitor'])

    def convertTable(self) -> pd.DataFrame:
        """
        Convert pdf table to pandas dataframe
        :return: dataframe
        """
        with pdfplumber.open(self.pdffile) as pdf:
            for i in range(len(pdf.pages)):
                first_page = pdf.pages[i]
                rawdata = first_page.extract_table()
                df = pd.DataFrame(rawdata)
                df.columns = df.iloc[0]
                df.drop(df.index[0], inplace=True)
                data = df[[*df.columns.drop([None, 'Steuernummer'])]]
                self.table = self.table.append(data)
            self.table.reset_index(drop=True, inplace=True)

        return self.table

    def writeTable2csv(self, outfilename: str = 'output.csv'):
        self.table.to_csv(outfilename, sep=";", encoding='utf-8')


if __name__ == "__main__":
    converter = TagUIDPdfConverter(file='../PDF/UID-Liste per 09.06.2021.pdf')
    converter.convertTable()
    converter.writeTable2csv()
