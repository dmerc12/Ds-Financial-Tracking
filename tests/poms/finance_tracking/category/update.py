from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for update category page
class UpdateCategoryPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for entering the name input on the update category page
    def enter_name_input(self, name):
        element: WebElement = self.driver.find_element(By.ID, 'name')
        return element.send_keys(name)

    ## POM for clicking the update category button on the update category page
    def click_update_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateCategoryButton')
        return element.click()

    ## POM for clicking the back button on the update category page
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()
