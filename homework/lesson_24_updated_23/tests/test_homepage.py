import time


def test_01_menu_bar_is_opened(homepage):
    homepage.open_menu()
    assert homepage._wait_for_element(('xpath', "//*[@class='navbar-nav']")).is_displayed()


def test_02_burger_menu_icon_is_replaced_by_x_icon(homepage):
    assert homepage._wait_for_element(('xpath', '//button[@class="icon f-navbtn"]')).is_displayed()


def test_03_logo_is_displayed(homepage):
    assert homepage.get_logo().is_displayed()


def test_04_click_on_logo_returns_to_homepage(homepage, driver):
    homepage.get_logo().click()
    assert driver.current_url == 'https://www.examples.com/'


def test_05_header_is_displayed_after_scrolling(homepage, driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    assert homepage.get_header().is_displayed()


def test_07_search_icon_is_displayed(homepage):
    assert homepage.get_search_icon().is_displayed()
    homepage.get_logo().click()


def test_08_search_field_is_displayed_after_clicking_on_search_icon(homepage):
    homepage.get_search_icon().click()
    assert homepage.get_search_field().is_displayed()
    homepage.get_logo().click()


def test_09_search_for_valid_text(homepage):
    homepage.get_search_icon().click()
    homepage.get_search_field().send_keys('test')
    time.sleep(3)
    assert homepage._wait_for_element(('xpath', '//h1')).text == 'Search Results for: test'
