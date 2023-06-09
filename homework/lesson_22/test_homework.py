from selenium.webdriver import Chrome
import time


def test_01_check_phone():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        call_us_xpath = "//*[@class='header-bar-nav_contacts']/button"
        phone_xpath = "//*[@id='headerTelContainer']/a"
        driver.find_element(by='xpath', value=call_us_xpath).click()
        text_phone = driver.find_element(by='xpath', value=phone_xpath).text
        phone = '0800 20 8020'

        assert text_phone == phone
    finally:
        driver.quit()


def test_02_check_email():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        call_us_xpath = "//*[@class='header-bar-nav_contacts']/button"
        email_xpath = "//*[@class='header-contacts-dropdown']/div[@class='header-contacts-dropdown_section']/a/span"
        driver.find_element(by='xpath', value=call_us_xpath).click()
        text_email = driver.find_element(by='xpath', value=email_xpath).text
        email = 'online@ithillel.ua'

        assert text_email == email
    finally:
        driver.quit()


def test_03_enroll_form_open():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        enroll_xpath = "//*[@id='btn-consultation-hero']"
        modal_xpath = '//*[@id="modal"]'
        driver.find_element(by='xpath', value=enroll_xpath).click()
        modal = driver.find_element(by='xpath', value=modal_xpath)
        assert modal.is_displayed()
    finally:
        driver.quit()


def test_04_enroll_form_empty_submit_button():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        enroll_xpath = "//*[@id='btn-consultation-hero']"
        driver.find_element(by='xpath', value=enroll_xpath).click()
        submit_button_xpath = '//*[@class="btn btn-submit -submit form-footer_btn"]'
        submit_button = driver.find_element(by='xpath', value=submit_button_xpath)
        assert submit_button.is_enabled() is False
    finally:
        driver.quit()


def test_05_enroll_form_populated_submit_button():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        enroll_xpath = "//*[@id='btn-consultation-hero']"
        driver.find_element(by='xpath', value=enroll_xpath).click()
        submit_button_xpath = '//*[@class="btn btn-submit -submit form-footer_btn"]'
        name_field_xpath = '//*[@id="input-name-consultation"]'
        email_field_xpath = '//*[@id="input-email-consultation"]'
        phone_field_xpath = '//*[@id="input-tel-consultation"]'
        course_select_xpath = '//*[@id="listbox-btn-input-course-consultation"]'
        course_list_xpath = '//*[@id="container-input-course-consultation"]/div/ul/li[10]'
        consent_checkbox_xpath = '//*[@id="form-consultation"]/div[@class="form_layout"]/footer/div' \
                                 '[@class="form_agreement"]/label/span'

        name_filed = driver.find_element(by='xpath', value=name_field_xpath)
        email_field = driver.find_element(by='xpath', value=email_field_xpath)
        phone_field = driver.find_element(by='xpath', value=phone_field_xpath)
        course_dropdown_select = driver.find_element(by='xpath', value=course_select_xpath)
        consent_checkbox = driver.find_element(by='xpath', value=consent_checkbox_xpath)
        submit_button = driver.find_element(by='xpath', value=submit_button_xpath)

        name_filed.send_keys('Test name')
        email_field.send_keys('email@email.email')
        phone_field.send_keys('986666666')
        course_dropdown_select.click()
        course_list = driver.find_element(by='xpath', value=course_list_xpath)
        course_list.click()
        consent_checkbox.click()

        assert submit_button.is_enabled() is True

    finally:
        driver.quit()


def test_06_enrollment_success_message():
    driver = Chrome('homework/lesson_22/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get('https://online.ithillel.ua/')
        enroll_xpath = "//*[@id='btn-consultation-hero']"
        driver.find_element(by='xpath', value=enroll_xpath).click()
        submit_button_xpath = '//*[@class="btn btn-submit -submit form-footer_btn"]'
        name_field_xpath = '//*[@id="input-name-consultation"]'
        email_field_xpath = '//*[@id="input-email-consultation"]'
        phone_field_xpath = '//*[@id="input-tel-consultation"]'
        course_select_xpath = '//*[@id="listbox-btn-input-course-consultation"]'
        course_list_xpath = '//*[@id="container-input-course-consultation"]/div/ul/li[10]'
        consent_checkbox_xpath = '//*[@id="form-consultation"]/div[@class="form_layout"]' \
                                 '/footer/div[@class="form_agreement"]/label/span'

        name_filed = driver.find_element(by='xpath', value=name_field_xpath)
        email_field = driver.find_element(by='xpath', value=email_field_xpath)
        phone_field = driver.find_element(by='xpath', value=phone_field_xpath)
        course_dropdown_select = driver.find_element(by='xpath', value=course_select_xpath)
        consent_checkbox = driver.find_element(by='xpath', value=consent_checkbox_xpath)
        submit_button = driver.find_element(by='xpath', value=submit_button_xpath)

        name_filed.send_keys('Test name')
        email_field.send_keys('email@email.email')
        phone_field.send_keys('986666666')
        course_dropdown_select.click()
        course_list = driver.find_element(by='xpath', value=course_list_xpath)
        course_list.click()
        consent_checkbox.click()

        submit_button.click()
        time.sleep(7)
        success_text = driver.find_element(by='xpath', value='//*[@class="p-xli c-green form-result_message"]')

        assert success_text.text == 'Відправлено'

    finally:
        driver.quit()

