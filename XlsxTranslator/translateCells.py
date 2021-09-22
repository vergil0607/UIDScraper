from Scraper import Scraper
import clipboard
from selenium.webdriver.common.keys import Keys


class TranslateCells:

    def __init__(self):
        self.scraper = Scraper()
        self.scraper.openURL('https://www.deepl.com')
        self.inputField = self.scraper.driver.find_element_by_css_selector('textarea[class="lmt__textarea '
                                                                           'lmt__source_textarea '
                                                                           'lmt__textarea_base_style"]')
        self.outputField = self.scraper.driver.find_element_by_id('target-dummydiv')

    def acceptCookies(self):
        self.scraper.driver.find_element_by_css_selector('button[class="dl_cookieBanner--buttonAll"]').click()

    def inputText(self, String):
        self.inputField.send_keys(String)

    def outputText(self):
        self.scraper.driver.find_element_by_css_selector('button[tabindex="130"]').click()
        outputString = clipboard.paste()
        outputString = outputString.replace('None', '')
        outputStringList = outputString.split('|')
        return outputStringList

    def clearInput(self):
        self.inputField.clear()
