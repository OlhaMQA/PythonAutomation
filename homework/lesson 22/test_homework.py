from selenium.webdriver import Chrome, Keys
import time

def test_01():
    driver = Chrome()
    driver.get('https://google.com')
    time.sleep(2)
    badge = '//*[@id="APjFqb"]'
    element = driver.find_element(by='xpath', value=badge)
    keys = element.send_keys('Test')
    element.send_keys(Keys.ENTER)
    locator_2 = '//*[@id="rso"]/div[8]/div/div/div[1]/div/a/h3'
    element_2 = driver.find_element(by='xpath', value=locator_2)
    element_2.click()

    time.sleep(5)

    driver.quit()

