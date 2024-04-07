from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for delete user page
class DeleteUserPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for clicking the back button on the delete user page
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()

    # POM for clicking the delete user button on delete user page
    def click_delete_user_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserButton')
        return element.click()
