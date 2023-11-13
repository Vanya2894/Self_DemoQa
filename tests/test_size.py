import time
from pages.demo_qa import DemoQa
from pages.elements_page import ElementsPage

def test_size(browser):
    size_demo = DemoQa(browser)
    size_demo.visit()

    browser.set_window_size(width=1000, height=300)
    time.sleep(2)
    browser.set_window_size(width=1000, height= 1000)

def test_visible_nav_bar(browser):
    mobile = ElementsPage(browser)
    mobile.visit()
    assert not mobile.nav.visible()
    browser.set_window_size(width=400, height=564)
    assert mobile.nav.visible()
    browser.set_window_size(width=1000,height=1000)
