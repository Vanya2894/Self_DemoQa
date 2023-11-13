import time

from pages.form_page import FormPage
from components.components import WebElement

def test_login_form(browser):
    form_log = FormPage(browser)

    form_log.visit()
    assert not form_log.modal_dialog.exist()
    time.sleep(10)
    form_log.first_name.send_keys('tester')
    form_log.last_name.send_keys('testerovich')
    form_log.user_email.send_keys('test@test.test')
    form_log.gender_radio_1.click_force()
    form_log.user_number.send_keys('7839371168')
    form_log.hobbies.click_force()
    form_log.current_address.send_keys('I am from England, my language is English')
    time.sleep(10)
    form_log.btn_submit.click_force()
    time.sleep(10)


    assert form_log.modal_dialog.exist()
    form_log.btn_close_modal.click_force()




