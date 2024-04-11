from poms.finance_tracking.deposit.manage_deposits import ManageDepositsPOMs
from poms.finance_tracking.expense.manage_expenses import ManageExpensesPOMs
from poms.finance_tracking.category.create import CreateCategoryPOMs
from poms.users.change_password import ChangePasswordPOMs
from selenium.webdriver.edge.webdriver import WebDriver
from poms.finance_tracking.home import FinanceHomePOMs
from poms.users.update import UpdateUserPOMs
from poms.users.register import RegisterPOMs
from poms.users.delete import DeleteUserPOMs
from poms.users.login import LoginPOMs
from poms.navbar import NavbarPOMs
from behave.runner import Context
from poms.home import HomePOMs

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()

    ## register POM files below
    # home poms
    context.home_poms = HomePOMs(context.driver)

    # track finances poms
    context.finance_poms = FinanceHomePOMs(context.driver)

    # users poms
    context.login_poms = LoginPOMs(context.driver)
    context.register_poms = RegisterPOMs(context.driver)
    context.change_password_poms = ChangePasswordPOMs(context.driver)
    context.update_user_poms = UpdateUserPOMs(context.driver)
    context.delete_user_poms = DeleteUserPOMs(context.driver)

    # category poms
    context.create_category_poms = CreateCategoryPOMs(context.driver)

    # deposit poms
    context.manage_deposits_poms = ManageDepositsPOMs(context.driver)

    # expense poms
    context.manage_expenses_poms = ManageExpensesPOMs(context.driver)

    # navigation poms
    context.navbar_poms = NavbarPOMs(context.driver)

    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
