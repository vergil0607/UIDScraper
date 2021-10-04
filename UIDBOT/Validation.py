from Scraper import Scraper
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


class Validation:

    def __init__(self):
        self.Scraper = Scraper()
        self.URL = "https://www.finanz.at/steuern/umsatzsteuer/uid-nummer/"
        self.Scraper.openURL(self.URL)

    def acceptCookies(self):
        time.sleep(2)
        frame = self.Scraper.driver.find_element_by_id('sp_message_iframe_545210')
        self.Scraper.driver.switch_to_frame(frame)
        self.Scraper.driver.find_elements_by_tag_name('button')[0].click()
        self.Scraper.driver.switch_to.default_content()

    def close_windows(self):
        time.sleep(2)
        try:
            self.Scraper.driver.find_element_by_id('pa-deny-btn').click()
        except NoSuchElementException:
            pass
        time.sleep(1)
        try:
            self.Scraper.driver.find_element_by_id('mitAds').click()
        except NoSuchElementException:
            pass

    def enterUID(self, UID):
        self.Scraper.driver.find_element_by_id('UID').clear()
        time.sleep(1)
        inputField = self.Scraper.driver.find_element_by_id('UID')
        inputField.send_keys(UID)
        time.sleep(1)
        self.Scraper.driver.find_element_by_id('checkUID').click()
        time.sleep(4)
        self.Scraper.driver.delete_all_cookies()

    def validateUID(self, UID):
        UIDValid = False
        self.enterUID(UID)
        if len(self.Scraper.driver.find_elements_by_class_name('bg-success')) > 1:
            UIDValid = True

        return UIDValid
