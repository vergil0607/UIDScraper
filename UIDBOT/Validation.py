from Scraper import Scraper
from selenium.webdriver.common.keys import Keys
import time


class Validation:

    def __init__(self):
        self.Scraper = Scraper()
        self.URL = "https://www.finanz.at/steuern/umsatzsteuer/uid-nummer/"
        self.Scraper.openURL(self.URL)

    def acceptCookies(self):
        time.sleep(2)
        frame = self.Scraper.driver.find_element_by_id('sp_message_iframe_416269')
        self.Scraper.driver.switch_to_frame(frame)
        self.Scraper.driver.find_elements_by_tag_name('button')[0].click()
        self.Scraper.driver.switch_to.default_content()

    def enterUID(self, UID):

        inputField = self.Scraper.driver.find_element_by_id('uidnummer')
        inputField.send_keys(UID)
        inputField.send_keys(Keys.ENTER)

    def returnToInputPage(self):
        self.Scraper.driver.find_element_by_css_selector('a[class="btn btn-warning"]').click()

    def validateUID(self, UID):

        UIDValid = False
        self.enterUID(UID)
        if self.Scraper.driver.find_elements_by_css_selector("span[class='text-white bg-success p-1 rounded']"):
            print('VALID')
        try:
            validationReturn = self.Scraper.driver.find_element_by_css_selector(
                "span[class='text-white bg-success p-1 rounded']")
            UIDValid = True
        except:
            pass
        self.returnToInputPage()

        return UIDValid
