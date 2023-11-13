import time

from pages.elements_page import ElementsPage
def test_visible_btn_sidebar(browser):
    visible = ElementsPage(browser)
    visible.visit()
    # visible.first_btn.click()
    # time.sleep(3)
    # assert visible.text_box.exist()
    assert visible.text_box.visible()

def test_not_visible_btn_sidebar(browser):
    visible_1 = ElementsPage(browser)
    visible_1.visit()
    assert visible_1.check_box.visible()
    visible_1.first_btn.click()
    time.sleep(3)
    assert not visible_1.check_box.visible()


