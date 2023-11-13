import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
class BasePage():
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url #'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title()

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False
