from pages.page_text_box import TextBox
import allure

@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    placeholder = TextBox(browser)

    placeholder.visit()
    assert placeholder.user_name.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 111 == 222
