import time

from pages.page_text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.user_name.send_keys('PETR')
    text_box.user_email.send_keys('pashtet@ya.ru')
    text_box.current_adress.send_keys('Малышка, крошка, бейба')
    text_box.permanent_address.send_keys('я ж тебя люблю')
    time.sleep(10)
    text_box.user_name.clear()
    text_box.user_email.clear()
    text_box.current_adress.clear()
    text_box.permanent_address.clear()
    time.sleep(10)
    assert text_box.user_name.get_text() == ''