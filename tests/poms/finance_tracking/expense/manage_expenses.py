from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for manage expenses page
class ManageExpensesPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the create expense link on the manage expenses page
    def click_create_expense_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'createExpenseLink')
        return element.click()

    ## POM for clicking the create category link on the manage expenses page
    def click_create_category_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'createCategoryLink')
        return element.click()

    ## POM for selecting category on the manage expenses page
    def select_category(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, 'category-select')
        select = Select(element)
        select.select_by_value(category_id)
        return select.first_selected_option.text

    ## POM for clicking the update category link on the manage expenses page
    def click_update_category_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'category-update-btn')
        return element.click()

    ## POM for clicking the delete category link on the manage expenses page
    def click_delete_category_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'category-delete-btn')
        return element.click()

    ## POM for clicking the search toggle on the manage expenses page
    def click_search_toggle(self):
        element: WebElement = self.driver.find_element(By.ID, 'search-toggle')
        return element.click()

    ## POM for inputting expense ID in search form on manage expenses page
    def input_expense_id_in_search(self, expense_id):
        element: WebElement = self.driver.find_element(By.ID, 'expense_id')
        return element.send_keys(expense_id)

    ## POM for inputting start date in search form on manage expenses page
    def input_start_date_in_search(self, start_date):
        element: WebElement = self.driver.find_element(By.ID, 'start_date')
        return element.send_keys(start_date)

    ## POM for inputting end date in search form on manage expenses page
    def input_end_date_in_search(self, end_date):
        element: WebElement = self.driver.find_element(By.ID, 'end_date')
        return element.send_keys(end_date)

    ## POM for clicking the search button on the manage expenses page
    def click_search_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'searchButton')
        return element.click()

    ## POM for clicking ID of given expense on manage expenses page
    def click_expense_id(self, expense_id):
        element: WebElement = self.driver.find_element(By.ID, 'expense-{expense_id}')
        return element.click()
