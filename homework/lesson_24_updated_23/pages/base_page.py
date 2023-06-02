from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework.lesson_24_updated_23.locators.header_locators import HeaderLocatorsCollection
from homework.lesson_24_updated_23.core.locator import Locator

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 5)

    def _wait_for_element(self, locator: Locator):
        return self._wait.until(EC.visibility_of_element_located(locator.to_tuple()))

    def click_element(self, locator: Locator):
        element = self._wait_for_element(locator.to_tuple())
        element.click()

    def send_keys(self, locator: Locator, text):
        element = self._wait_for_element(locator.to_tuple())
        element.send_keys(text)

    def get_menu_button(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.burger_menu))
        return element

    def open_menu(self):
        self.get_menu_button().click()

    def close_menu(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.close_menu))
        element.click()

    def get_logo(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.logo))
        return element

    def get_header(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.header))
        return element

    def get_search_icon(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.search_icon))
        return element

    def get_search_field(self):
        element = self._wait_for_element(Locator(HeaderLocatorsCollection.search_field))
        return element

