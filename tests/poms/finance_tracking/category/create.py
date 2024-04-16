from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for create category page
class CreateCategoryPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for entering the name input on the create category page
    def enter_name_input(self, name):
        element: WebElement = self.driver.find_element(By.ID, 'name')
        return element.send_keys(name)

    ## POM for clicking the create category button on the create category page
    def click_create_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'createCategoryButton')
        return element.click()

