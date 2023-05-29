from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 5)

    def _wait_for_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def get_menu_button(self):
        element = self._wait_for_element(('xpath', '//button[@aria-label="menu"]'))
        return element

    def open_menu(self):
        self.get_menu_button().click()

    def close_menu(self):
        element = self._wait_for_element(('xpath', '//button[@class="icon f-navbtn"]'))
        element.click()

    def get_logo(self):
        element = self._wait_for_element(('xpath', '//img[@alt="Examples.com"]'))
        return element

    def get_header(self):
        element = self._wait_for_element(('xpath', '//header'))
        return element

    def get_search_icon(self):
        element = self._wait_for_element(('xpath', '//button[@class="icon search-iocn"]'))
        return element

    def get_search_field(self):
        element = self._wait_for_element(('xpath', '//input[@id="headerSearch"]'))
        return element

    def click_element(self, locator):
        element = self._wait_for_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self._wait_for_element(locator)
        element.send_keys(text)