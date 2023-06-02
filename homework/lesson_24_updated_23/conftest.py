from selenium.webdriver import Chrome
from homework.lesson_23.pages.homepage import Homepage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('homework/lesson 22/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.examples.com/')
    yield driver
    driver.quit()


@pytest.fixture
def homepage(driver):
    yield Homepage(driver)
