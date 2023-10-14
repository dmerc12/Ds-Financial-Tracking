from behave.runner import Context
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver
from Tests.POMs.CategoryPOMs import CategoryPOMs

def before(context: Context):
    context.driver = WebDriver()
    context.category_poms = CategoryPOMs(context.driver)
    context.driver.implicitly_wait(1)

def after(context: Context):
    context.driver.close()
