from pages.base_page import BasePage
from components.components import WebElement
class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, '#alertButton')
        self.confirmButton = WebElement(driver, '#confirmButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.promtButton = WebElement(driver, '#promtButton')
        self.promptResult = WebElement(driver, '#promptResult')
