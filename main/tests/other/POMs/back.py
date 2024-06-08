from selenium.webdriver.common.by import By
from tests.other.POMs import navigation

# POM for change password back button
def change_password_back(self, title, username, password):
    navigation.navigate_change_password(self, 'Changing Password', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete user back button
def delete_user_back(self, title, username, password):
    navigation.navigate_delete_user(self, 'Deleting Account', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for create deposit category back button
def create_deposit_category_back(self, title, username, password):
    navigation.navigate_create_deposit_category(self, 'Adding Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for update deposit category back button
def update_deposit_category_back(self, title, username, password):
    navigation.navigate_update_deposit_category(self, 'Updating Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete deposit category back button
def delete_deposit_category_back(self, title, username, password):
    navigation.navigate_delete_deposit_category(self, 'Deleting Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for create deposit back button
def create_deposit_back(self, title, username, password):
    navigation.navigate_create_deposit(self, 'Creating Deposit', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for deposit detail back button
def deposit_detail_back(self, title, username, password):
    ID = 13
    navigation.navigate_deposit_detail(self, f'Deposit - {ID}', username, password, ID)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for update deposit back button
def update_deposit_back(self, title, username, password):
    navigation.navigate_update_deposit(self, 'Updating Deposit', username, password, 14)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete deposit back button
def delete_deposit_back(self, title, username, password):
    navigation.navigate_delete_deposit(self, 'Deleting Deposit', username, password, 12)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for create expense category back button
def create_expense_category_back(self, title, username, password):
    navigation.navigate_create_expense_category(self, 'Adding Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for update expense category back button
def update_expense_category_back(self, title, username, password):
    navigation.navigate_update_expense_category(self, 'Updating Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete expense category back button
def delete_expense_category_back(self, title, username, password):
    navigation.navigate_delete_expense_category(self, 'Deleting Category', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for create expense back button
def create_expense_back(self, title, username, password):
    navigation.navigate_create_expense(self, 'Creating Expense', username, password)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for expense detail back button
def expense_detail_back(self, title, username, password):
    ID = 13
    navigation.navigate_expense_detail(self, f'Expense - {ID}', username, password, ID)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for update expense back button
def update_expense_back(self, title, username, password):
    navigation.navigate_update_expense(self, 'Updating Expense', username, password, 14)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete expense back button
def delete_expense_back(self, title, username, password):
    navigation.navigate_delete_expense(self, 'Deleting Expense', username, password, 12)
    self.driver.find_element(By.ID, 'backButton').click()
    self.assertEqual(self.driver.title, title)
