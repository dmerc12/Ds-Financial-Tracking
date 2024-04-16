from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for delete category page
class DeleteCategoryPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the delete category button on the delete category page
    def click_delete_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteCategoryButton')
        return element.click()
