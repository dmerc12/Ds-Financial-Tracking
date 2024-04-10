from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for login page
class LoginPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for clicking the register link on the login page
    def click_register_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'registerLink')
        return element.click()

    # POM for entering the username input on the login page
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)

    # POM for entering the password input on the login page
    def enter_password_input(self, password):
        element: WebElement = self.driver.find_element(By.ID, 'password')
        return element.send_keys(password)

    # POM for clicking the login button on the login page
    def click_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'loginButton')
        return element.click()
