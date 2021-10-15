from Scraper import Scraper
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Validation:

    def __init__(self):
        self.Scraper = Scraper()
        self.URL = "https://ec.europa.eu/taxation_customs/vies/vatResponse.html"
        self.Scraper.openURL(self.URL)
        time.sleep(2)

    def selectCountry(self, countrycode):
        select = Select(self.Scraper.driver.find_element_by_id('countryCombobox'))
        select.select_by_value(countrycode)

    def enterNumber(self, number):
        inputfield = self.Scraper.driver.find_element_by_id('number')
        inputfield.clear()
        inputfield.send_keys(number)

    def pruefen(self):
        self.Scraper.driver.find_element_by_id('submit').click()

    def checkValidity(self):
        valid_class_elements = self.Scraper.driver.find_elements_by_class_name('validStyle')
        if valid_class_elements:
            return True
        else:
            return False

    def returnPage(self):
        self.Scraper.driver.back()

    def makeRequest(self, UID):
        """
        make a full request for validity of UID
        :param UID:
        :return: validity (True if the UID was found)
        """
        countrycode = UID[:2]
        number = UID[2:]
        self.selectCountry(countrycode)
        self.enterNumber(number)
        self.pruefen()
        time.sleep(2)
        validity = self.checkValidity()
        self.returnPage()
        time.sleep(2)
        return validity


