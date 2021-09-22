from selenium import webdriver


class Scraper:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Wieser\Documents\Configs\chromedriver.exe')

    def openURL(self, URL):
        self.driver.get(URL)

