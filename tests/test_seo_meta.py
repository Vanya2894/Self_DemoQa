import time
import pytest
from pages.demo_qa import DemoQa
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize('pages', [Alerts, DemoQa, BrowserTab])
def test_title_all_page(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(3)

    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'