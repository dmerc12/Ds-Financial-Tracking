from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for deposit detail page
class DepositDetailPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking update deposit button on deposit detail page
    def click_update_deposit_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateDepositLink')
        return element.click()

    ## POM for clicking delete deposit button on deposit detail page
    def click_delete_deposit_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteDepositLink')
        return element.click()
