from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from UIDBOT.parameters import Parameters


class Scraper:

    def __init__(self):
        if Parameters.usebrowser:
            self.driver = webdriver.Chrome(executable_path=Parameters.chromepath)
        else:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=Parameters.chromepath,
                                           options=self.chrome_options)

    def openURL(self, url):
        self.driver.get(url)


