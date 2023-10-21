from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver

class DepositPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_manage_deposits_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageDepositsNavButton")
        return element.click()

    def click_manage_deposits_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageDepositsButton")
        return element.click()

    def click_create_deposit_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createDepositModal")
        return element.click()

    def select_create_deposit_category_id(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, "createDepositCategoryInput")
        return element.send_keys(category_id)

    def input_create_deposit_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, "createDepositDateInput")
        return element.send_keys(date)

    def input_create_deposit_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, "createDepositDescriptionInput")
        return element.send_keys(description)

    def input_create_deposit_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, "createDepositAmountInput")
        return element.send_keys(amount)

    def click_create_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createDepositButton")
        return element.click()

    def click_update_deposit_modal(self, deposit_id):
        element: WebElement = self.driver.find_element(By.ID, f"updateDepositModal{deposit_id}")
        return element.click()

    def select_update_deposit_category_id(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, "updateDepositCategoryInput")
        return element.send_keys(category_id)

    def input_update_deposit_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, "updateDepositDateInput")
        return element.send_keys(date)

    def input_update_deposit_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, "updateDepositDescriptionInput")
        return element.send_keys(description)

    def input_update_deposit_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, "updateDepositAmountInput")
        return element.send_keys(amount)

    def click_update_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateDepositButton")
        return element.click()

    def click_delete_deposit_modal(self, deposit_id):
        element: WebElement = self.driver.find_element(By.ID, f"deleteDepositModal{deposit_id}")
        return element.click()

    def click_delete_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteDepositButton")
        return element.click()
