from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for delete deposit page
class DeleteDepositPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking delete deposit button on delete deposit page
    def click_delete_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteDepositButton')
        return element.click()

    ## POM for clicking back button on delete deposit page
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()
