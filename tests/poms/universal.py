from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# universal POMs
class UniversalPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the search toggle
    def click_search_toggle(self):
        element: WebElement = self.driver.find_element(By.ID, 'search-toggle')
        return element.click()

    ## POM for clicking the back button
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()
