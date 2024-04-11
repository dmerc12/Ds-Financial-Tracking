from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for navbar
class NavbarPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for home button in the navbar
    def click_home_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'home')
        return element.click()

    ## POM for manage info button in the navbar
    def click_manage_info_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'manageInfo')
        return element.click()

    ## POM for track finances dropdown in the navbar
    def click_track_finances_toggle(self):
        element: WebElement = self.driver.find_element(By.ID, 'trackFinancesDropdown')
        return element.click()

    ## POM for deposit home button in the navbar
    def click_deposit_home_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'depositHome')
        return element.click()

    ## POM for expense home button in the navbar
    def click_expense_home_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'expenseHome')
        return element.click()

    ## POM for view finances button in the navbar
    def click_view_finances_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'viewFinances')
        return element.click()

    ## POM for analyze finances button in the navbar
    def click_analyze_finances_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'analyzeFinances')
        return element.click()

    ## POM for logout button in the navbar
    def click_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'logoutButton')
        return element.click()

    ## POM for register button in the navbar
    def click_register_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'register')
        return element.click()

    ## POM for login button in the navbar
    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'login')
        return element.click()
