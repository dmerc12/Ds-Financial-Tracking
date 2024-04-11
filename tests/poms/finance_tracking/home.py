from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for finance home page
class FinanceHomePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the manage deposits link on the finance home page
    def click_manage_deposits_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'depositHomeLink')
        return element.click()

    ## POM for clicking the manage expenses link on the finance home page
    def click_manage_expenses_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'expenseHomeLink')
        return element.click()

    ## POM for clicking the view finances link on the finance home page
    def click_view_finances_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'viewFinancesLink')
        return element.click()

    ## POM for clicking the analyze finances link on the finance home page
    def click_analyze_finances_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'analyzeFinancesLink')
        return element.click()
