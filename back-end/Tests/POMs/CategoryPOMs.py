from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver

class CategoryPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_manage_categories_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCategoriesNavButton")
        return element.click()

    def click_manage_categories_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageCategoriesButton")
        return element.click()

    def click_create_category_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryModal")
        return element.click()

    def input_create_category_name(self, category_name):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryNameInput")
        return element.send_keys(category_name)

    def click_create_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createCategoryButton")
        return element.click()

    def click_update_category_modal(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, f"updateCategoryModal{category_id}")
        return element.click()

    def input_update_category_name(self, category_name):
        element: WebElement = self.driver.find_element(By.ID, "updateCategoryNameInput")
        return element.send_keys(category_name)

    def click_update_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateCategoryButton")
        return element.click()

    def click_delete_category_modal(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, f"deleteCategoryModal{category_id}")
        return element.click()

    def click_delete_category_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteCategoryButton")
        return element.click()
