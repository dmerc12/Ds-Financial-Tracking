from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for update user page
class UpdateUserPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking the change password link on the update user page
    def click_change_password_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'changePasswordLink')
        return element.click()

    ## POM for clicking the delete user link on the update user page
    def click_delete_user_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteUserLink')
        return element.click()

    ## POM for entering the username input on the update user page
    def enter_username_input(self, username):
        element: WebElement = self.driver.find_element(By.ID, 'username')
        return element.send_keys(username)

    ## POM for entering the first name input on the update user page
    def enter_first_name_input(self, first_name):
        element: WebElement = self.driver.find_element(By.ID, 'first_name')
        return element.send_keys(first_name)

    ## POM for entering the last name input on the update user page
    def enter_last_name_input(self, last_name):
        element: WebElement = self.driver.find_element(By.ID, 'last_name')
        return element.send_keys(last_name)

    ## POM for entering the email input on the update user page
    def enter_email_input(self, email):
        element: WebElement = self.driver.find_element(By.ID, 'email')
        return element.send_keys(email)

    ## POM for entering the phone number input on the update user page
    def enter_phone_number_input(self, phone_number):
        element: WebElement = self.driver.find_element(By.ID, 'phone_number')
        return element.send_keys(phone_number)

    ## POM for clicking the update user button on the update user page
    def click_update_user_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateUserButton')
        return element.click()
