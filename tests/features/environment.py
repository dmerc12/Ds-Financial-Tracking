from tests.poms.finance_tracking.deposit.manage_deposits import ManageDepositsPOMs
from tests.poms.finance_tracking.expense.manage_expenses import ManageExpensesPOMs
from tests.poms.finance_tracking.category.create import CreateCategoryPOMs
from tests.poms.finance_tracking.category.update import UpdateCategoryPOMs
from tests.poms.users.change_password import ChangePasswordPOMs
from tests.poms.finance_tracking.home import FinanceHomePOMs
from selenium.webdriver.edge.webdriver import WebDriver
from tests.poms.users.update import UpdateUserPOMs
from tests.poms.users.register import RegisterPOMs
from tests.poms.users.delete import DeleteUserPOMs
from tests.poms.users.login import LoginPOMs
from tests.poms.navbar import NavbarPOMs
from tests.poms.home import HomePOMs
from behave.runner import Context

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
    context.update_category_poms = UpdateCategoryPOMs(context.driver)

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
