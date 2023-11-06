import time
from pages.elements_page import ElementsPage
from components.components import WebElement
def test_page_elements(browser):
    elem = ElementsPage(browser)
    elem.visit()
    time.sleep(3)

    assert elem.header.get_text() == 'Elements'
    assert elem.icon_head.exist()
    assert elem.first_btn.exist()
    assert elem.text_box.exist()
