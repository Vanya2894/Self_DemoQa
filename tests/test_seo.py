import time
import pytest
from pages.demo_qa import DemoQa
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab



def test_seo(browser):
    demo = DemoQa(browser)
    demo.visit()

    assert browser.title == 'DEMOQA'

@pytest.mark.skip
@pytest.mark.parametrize('pages', [Alerts, DemoQa, BrowserTab])
def test_title_all_page(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(3)
    assert page.get_title() == 'DEMOQA'
