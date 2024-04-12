from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for home page
class HomePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the manage info button on the home page
    def click_manage_information_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'manageInfoButton')
        return element.click()

    ## POM for clicking the track finances button on the home page
    def click_track_finances_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'trackFinancesButton')
        return element.click()
