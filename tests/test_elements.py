from pages.elements_page import ElementsPage
from pages.checkbox_page import CheckBox

def test_find_elements(browser):
    elem_page = ElementsPage(browser)
    elem_page.visit()

    assert elem_page.btns_first_menu.check_count_elements(count=9)

def test_count_checkbox(browser):
    checkbox_page = CheckBox(browser)
    checkbox_page.visit()
    assert checkbox_page.checkbox.check_count_elements(count=1)
    checkbox_page.btn_expand_all.click()
    assert checkbox_page.checkbox.check_count_elements(count=17)
    browser.refresh()
    assert checkbox_page.checkbox.check_count_elements(count=1)


