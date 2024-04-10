from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for register page
class RegisterPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # POM for clicking the login link on the register page
    def click_login_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'loginLink')
        return element.click()

    # POM for entering the username input on the register page
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)

    # POM for entering the first name input on the register page
    def enter_first_name_input(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, 'first_name')
        return element.send_keys(first_name)

    # POM for entering the last name input on the register page
    def enter_last_name_input(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, 'last_name')
        return element.send_keys(last_name)

    # POM for entering the email input on the register page
    def enter_email_input(self, email):
        element: WebElement = self.driver.find_element(By.ID, 'email')
        return element.send_keys(email)

    # POM for entering the phone number input on the register page
    def enter_phone_number_input(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, 'phone_number')
        return element.send_keys(phone_number)

    # POM for entering the password 1 input on the register page
    def enter_password1_input(self, password1):
        element: WebElement = self.driver.find_element(By.ID, 'password1')
        return element.send_keys(password1)

    # POM for entering the password 2 input on the register page
    def enter_password2_input(self, password2):
        element: WebElement = self.driver.find_element(By.ID, 'password2')
        return element.send_keys(password2)

    # POM for clicking the register button on the register page
    def click_register_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'registerButton')
        return element.click()
