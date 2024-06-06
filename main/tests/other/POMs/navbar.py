from selenium.webdriver.common.by import By
from tests.users.POMs.login import login

# POM for home redirect
def home_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'home').click()
    self.assertEqual(self.driver.title, title)

# POM for home success
def home_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'home').click()
    self.assertEqual(self.driver.title, title)

# POM for manage info redirect
def manage_info_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'manageInfo').click()
    self.assertEqual(self.driver.title, title)

# POM for manage info success
def manage_info_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfo').click()
    self.assertEqual(self.driver.title, title)

# POM for manage deposits redirect
def manage_deposits_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'depositHome').click()
    self.assertEqual(self.driver.title, title)

# POM for manage deposits success
def manage_deposits_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'depositHome').click()
    self.assertEqual(self.driver.title, title)

# POM for manage expenses redirect
def manage_expenses_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'expenseHome').click()
    self.assertEqual(self.driver.title, title)

# POM for manage expenses success
def manage_expenses_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'expenseHome').click()
    self.assertEqual(self.driver.title, title)

# POM for view finances redirect
def view_finances_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'viewFinances').click()
    self.assertEqual(self.driver.title, title)

# POM for view finances success
def view_finances_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'viewFinances').click()
    self.assertEqual(self.driver.title, title)

# POM for analyze finances redirect
def analyze_finances_redirect(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'analyzeFinances').click()
    self.assertEqual(self.driver.title, title)

# POM for analyze finances success
def analyze_finances_success(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesDropdown').click()
    self.driver.find_element(By.ID, 'analyzeFinances').click()
    self.assertEqual(self.driver.title, title)

# POM for logout
def logout(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'logoutButton').click()
    self.assertEqual(self.driver.title, title)
