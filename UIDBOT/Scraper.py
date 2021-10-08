from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper:

    def __init__(self, headless=True):
        if headless:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=r'C:\Users\Wieser\Documents\Configs\chromedriver.exe',
                                           options=self.chrome_options)
        else:
            self.driver = webdriver.Chrome(executable_path=r'C:\Users\Wieser\Documents\Configs\chromedriver.exe')

    def openURL(self, url):
        self.driver.get(url)
