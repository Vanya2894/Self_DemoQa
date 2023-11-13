from pages.base_page import BasePage
from components.components import WebElement
class CheckBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.checkbox = WebElement(driver, locator='span.rct-title')
        self.btn_expand_all = WebElement(driver, locator='button.rct-option.rct-option-expand-all > svg')
