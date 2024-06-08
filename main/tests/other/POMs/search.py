from selenium.webdriver.common.by import By
from tests.other.POMs import navigation

# POM for search finances from analyze finances page
def search_analyze_finances(self, title, username, password, start_date, end_date):
    navigation.navigate_analyze_finances(self, 'Analyzing Finances', username, password)
    self.driver.find_element(By.NAME, 'start_date').send_keys(start_date)
    self.driver.find_element(By.NAME, 'end_date').send_keys(end_date)
    self.driver.find_element(By.ID, 'searchButton').click()
    self.assertEqual(self.driver.title, title)
