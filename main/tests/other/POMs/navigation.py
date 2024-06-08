from tests.category.POMs.create import create_deposit_category, create_expense_category
from tests.deposit.POMs.create import create_deposit
from tests.expense.POMs.create import create_expense
from selenium.webdriver.common.by import By
from tests.users.POMs.login import login
from datetime import datetime

# POM for navigating using sign up link
def navigate_sign_up_link(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'registerLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating using log in link
def navigate_log_in_link(self, title):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'registerLink').click()
    self.driver.find_element(By.ID, 'loginLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to manage info page
def navigate_manage_info(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to change password page
def navigate_change_password(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    self.driver.find_element(By.ID, 'changePasswordLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to delete user page
def navigate_delete_user(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    self.driver.find_element(By.ID, 'deleteUserLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to track finances page
def navigate_track_finances(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to create deposit category page
def navigate_create_deposit_category(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'depositHomeLink').click()
    self.driver.find_element(By.ID, 'createCategoryLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to update deposit category page
def navigate_update_deposit_category(self, title, username, password):
    create_deposit_category(self, 'Managing Deposits', username, password, 'test')
    self.driver.find_element(By.ID, 'category-update-btn').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to delete deposit category page
def navigate_delete_deposit_category(self, title, username, password):
    create_deposit_category(self, 'Managing Deposits', username, password, 'test')
    self.driver.find_element(By.ID, 'category-delete-btn').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to create expense category page
def navigate_create_expense_category(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'expenseHomeLink').click()
    self.driver.find_element(By.ID, 'createCategoryLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to update expense category page
def navigate_update_expense_category(self, title, username, password):
    create_expense_category(self, 'Managing Expenses', username, password, 'test')
    self.driver.find_element(By.ID, 'category-update-btn').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to delete expense category page
def navigate_delete_expense_category(self, title, username, password):
    create_expense_category(self, 'Managing Expenses', username, password, 'test')
    self.driver.find_element(By.ID, 'category-delete-btn').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to manage deposits page
def navigate_manage_deposits(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'depositHomeLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to deposit detail page
def navigate_deposit_detail(self, title, username, password, ID):
    create_deposit(self, 'Managing Deposits', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'deposit-{ID}').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to create deposit page
def navigate_create_deposit(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'depositHomeLink').click()
    self.driver.find_element(By.ID, 'createDepositLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to update deposit page
def navigate_update_deposit(self, title, username, password, ID):
    create_deposit(self, 'Managing Deposits', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'deposit-{ID}').click()
    self.driver.find_element(By.ID, 'updateDepositLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to delete deposit page
def navigate_delete_deposit(self, title, username, password, ID):
    create_deposit(self, 'Managing Deposits', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'deposit-{ID}').click()
    self.driver.find_element(By.ID, 'deleteDepositLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to manage expenses page
def navigate_manage_expenses(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'expenseHomeLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to expense detail page
def navigate_expense_detail(self, title, username, password, ID):
    create_expense(self, 'Managing Expenses', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'expense-{ID}').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to create expense page
def navigate_create_expense(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'expenseHomeLink').click()
    self.driver.find_element(By.ID, 'createExpenseLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to update expense page
def navigate_update_expense(self, title, username, password, ID):
    create_expense(self, 'Managing Expenses', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'expense-{ID}').click()
    self.driver.find_element(By.ID, 'updateExpenseLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to delete expense page
def navigate_delete_expense(self, title, username, password, ID):
    create_expense(self, 'Managing Expenses', username, password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
    self.driver.find_element(By.ID, f'expense-{ID}').click()
    self.driver.find_element(By.ID, 'deleteExpenseLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to view finances page
def navigate_view_finances(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'viewFinancesLink').click()
    self.assertEqual(self.driver.title, title)

# POM for navigating to analyze finances page
def navigate_analyze_finances(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'analyzeFinancesLink').click()
    self.assertEqual(self.driver.title, title)
