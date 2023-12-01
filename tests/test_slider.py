import time
from selenium.webdriver.common.keys import Keys

from pages.slider_page import Slider
from selenium.webdriver import ActionChains

def test_slider_v1(browser):
    slider = Slider(browser)
    action_chains = ActionChains(browser)
    slider.visit()

    assert slider.slider_cont.exist()
    assert slider.slider_value.exist()
    time.sleep(10)

    action_chains.drag_and_drop_by_offset(slider.slider_cont.find_element(), xoffset=0, yoffset=1).perform()
    time.sleep(10)
    assert slider.slider_value.get_dom_attribute('value') == '50'


def test_slider_v2(browser):
    slider = Slider(browser)
    action_chains = ActionChains(browser)
    slider.visit()

    assert slider.slider_cont.exist()
    assert slider.slider_value.exist()
    time.sleep(10)

    while not slider.slider_value.get_dom_attribute('value') == '50':
            slider.slider_cont.send_keys(Keys.ARROW_RIGHT)

    assert slider.slider_value.get_dom_attribute('value') == '50'




