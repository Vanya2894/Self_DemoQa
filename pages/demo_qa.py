from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver,self.base_url)
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_elements = WebElement(driver, locator='div.home-body > div > div:nth-child(1)')

        self.h5 = WebElement(driver, 'div h5')


    # def exist_icon(self):
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.find_element(locator='#app > header > a').click()
    #
    #
    # def click_on_the_btn_elements(self):
    #     self.find_element(locator='div.home-body > div > div:nth-child(1)').click()
