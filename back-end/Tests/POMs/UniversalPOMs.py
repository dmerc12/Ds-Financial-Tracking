from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver

class UniversalPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_home_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "homeNavButton")
        return element.click()

    def toast_notification_text(self):
        element: WebElement = self.driver.find_element(By.CLASS_NAME, "toast")
        return element.text
