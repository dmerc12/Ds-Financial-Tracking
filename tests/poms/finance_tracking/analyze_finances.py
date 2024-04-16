from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for analyze finances page
class AnalyzeFinancesPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for inputting start date in search form on analyze finances page
    def enter_start_date_in_search_input(self, start_date):
        element: WebElement = self.driver.find_element(By.ID, 'start_date')
        return element.send_keys(start_date)

    ## POM for inputting end date in search form on analyze finances page
    def enter_end_date_in_search_input(self, end_date):
        element: WebElement = self.driver.find_element(By.ID, 'end_date')
        return element.send_keys(end_date)

    ## POM for clicking the search button on the analyze finances page
    def click_search_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'searchButton')
        return element.click()
