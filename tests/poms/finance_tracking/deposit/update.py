from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for update deposit page
class UpdateDepositPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking update deposit button on update deposit page
    def click_update_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateDepositButton')
        return element.click()

    ## POM for clicking back button on update deposit page
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()
