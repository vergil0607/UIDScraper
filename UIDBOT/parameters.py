"""
define all parameters relevant parameters for the automation
"""


class Parameters:

    PATH = r"C:\Users\Wieser\Documents\Projekte\TAG\2021\RPA\UID Use Case\202106_Python\UIDBOT"
    chromepath = r'C:\Users\Wieser\Documents\Configs\chromedriver.exe'
    filein = "ValidatedUIDs.xlsx"
    fileout = "ValidatedUIDs_Output.xlsx"
    check_all = True
    usebrowser = True

    def __init__(self):
        pass
