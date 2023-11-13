from pages.demo_qa import DemoQa

def test_seo(browser):
    demo = DemoQa(browser)
    demo.visit()

    assert browser.title == 'DEMOQA'