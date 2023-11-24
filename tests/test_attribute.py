from pages.page_text_box import TextBox

def test_placeholder(browser):
    placeholder = TextBox(browser)

    placeholder.visit()
    assert placeholder.user_name.get_dom_attribute('placeholder') == 'Full Name'


