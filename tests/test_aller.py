import time

from pages.alerts import Alerts
def test_alerts(browser):
    alert = Alerts(browser)

    alert.visit()
    time.sleep(10)
    assert not alert.alert()

    alert.btn_alert.click()
    time.sleep(10)
    assert alert.alert()
    alert.alert().accept()

def test_alert_text(browser):
    two_alert = Alerts(browser)

    two_alert.visit()
    two_alert.btn_alert.click()
    time.sleep(3)
    assert two_alert.alert().text == 'You clicked a button'
    two_alert.alert().accept()
    assert not two_alert.alert()

def test_confirm(browser):
    three_alert = Alerts(browser)
    three_alert.visit()

    three_alert.confirmButton.click()
    time.sleep(3)
    three_alert.alert().dismiss()
    assert three_alert.confirmResult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    four_alert = Alerts(browser)

    four_alert.visit()
    four_alert.promtButton.click()
    time.sleep(3)
    four_alert.alert().send_keys('Ivan')
    four_alert.alert().accept()
    assert four_alert.promptResult.get_text() == 'You entered Ivan'
    time.sleep(3)
