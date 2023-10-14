from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver

class CategoryPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manage_categories_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCategoriesButton")
        return element

    def create_category_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryModal")
        return element

    def create_category_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryNameInput")
        return element

    def create_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryButton")
        return element

    def update_category_modal(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, f"updateCategoryModal{category_id}")
        return element

    def update_category_name_input(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCategoryNameInput")
        return element

    def update_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCategoryButton")
        return element

    def delete_category_modal(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, f"deleteCategoryModal{category_id}")
        return element

    def delete_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteCategoryButton")
        return element
