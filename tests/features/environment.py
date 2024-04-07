from selenium.webdriver.edge.webdriver import WebDriver
from poms.users.change_password import ChangePasswordPOMs
from poms.users.update import UpdateUserPOMs
from poms.users.register import RegisterPOMs
from poms.users.delete import DeleteUserPOMs
from poms.users.login import LoginPOMs
from poms.navbar import NavbarPOMs
from behave.runner import Context

# Setup for webdriver and POM files before selenium tests
def before_all(context: Context):
    context.driver = WebDriver()

    ## register POM files below
    # users poms
    context.login_poms = LoginPOMs(context.driver)
    context.register_poms = RegisterPOMs(context.driver)
    context.change_password_poms = ChangePasswordPOMs(context.driver)
    context.update_user_poms = UpdateUserPOMs(context.driver)
    context.delete_user_poms = DeleteUserPOMs(context.driver)

    # category poms

    # deposit poms

    # expense poms

    # navigation poms
    context.navbar_poms = NavbarPOMs(context.driver)

    context.driver.implicitly_wait(1)

# Cleanup for webdriver after selenium tests
def after_all(context: Context):
    context.driver.close()
