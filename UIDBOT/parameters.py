"""
define all parameters relevant parameters for the automation
"""


class Parameters:

    chromepath = r'C:\Users\Wieser\Documents\Configs\chromedriver.exe'
    PATH = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\202106_Python\files"
    filein = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\202106_Python\files\BNI_UID_Liste.xlsx"  # "ATU Prüfung 2021.xlsx"
    fileout = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\202106_Python\files\BNI_UID_Liste_checked.xlsx"  # "ValidatedUIDs_Output.xlsx"
    check_all = True
    Limit = 200
    usebrowser = True
    tabname = 'Tabelle1'  # 'Table 1'
    newcolix = 4  # 6
    newcolumn = 'D1'  # F1

    def __init__(self):
        pass
