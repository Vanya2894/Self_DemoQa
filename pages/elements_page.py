from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.header = WebElement(driver,locator='#app > div > div > div.pattern-backgound.playgound-header > div')
        self.icon_head = WebElement(driver, locator='#app > header > a > img')
        self.first_btn = WebElement(driver, locator='div:nth-child(1) > span > div')
        self.text_box = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-0 > span')
        self.check_box = WebElement(driver, locator= 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li')
        self.nav = WebElement(driver, locator='div > nav')




