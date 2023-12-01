from pages.base_page import BasePage
from components.components import WebElement

class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, '#app div:nth-child(2) > label')
        self.text = WebElement(driver, '#app > div > div div:nth-child(2) > p')
        self.impressive = WebElement(driver, '#app div:nth-child(3) > label')
        self.no = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div.custom-control.disabled.custom-radio.custom-control-inline > label')


