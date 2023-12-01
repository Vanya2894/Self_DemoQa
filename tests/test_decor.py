import pytest
from pages.demo_qa import DemoQa
from pages.radio_page import Radio

def test_decor(browser):
    decor = DemoQa(browser)
    decor.visit()

    assert decor.h5.check_count_elements(6)

    for element in decor.h5.find_elements():
        assert element.text != ''


# @pytest.mark.skipif(True, reason='просто пропуск')
def test_skip_if(browser):
    radio = Radio(browser)

    if not radio.code_status():
        pytest.skip(reason=f'страница {radio.base_url} недоступна')

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio.no.get_dom_attribute('class')

# def test_decor(browser):
#     pytest.skip()


