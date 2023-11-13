from pages.demo_qa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    navi = DemoQa(browser)
    elem_pg = ElementsPage(browser)

    navi.visit()
    navi.btn_elements.click()

    navi.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    elem_pg.equal_url()


