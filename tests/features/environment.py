from tests.poms.finance_tracking.deposit.manage_deposits import ManageDepositsPOMs
from tests.poms.finance_tracking.expense.manage_expenses import ManageExpensesPOMs
from tests.poms.finance_tracking.analyze_finances import AnalyzeFinancesPOMs
from tests.poms.finance_tracking.category.create import CreateCategoryPOMs
from tests.poms.finance_tracking.category.update import UpdateCategoryPOMs
from tests.poms.finance_tracking.category.delete import DeleteCategoryPOMs
from tests.poms.finance_tracking.deposit.create import CreateDepositPOMs
from tests.poms.finance_tracking.deposit.update import UpdateDepositPOMs
from tests.poms.finance_tracking.deposit.delete import DeleteDepositPOMs
from tests.poms.finance_tracking.deposit.detail import DepositDetailPOMs
from tests.poms.finance_tracking.expense.create import CreateExpensePOMs
from tests.poms.finance_tracking.expense.update import UpdateExpensePOMs
from tests.poms.finance_tracking.expense.delete import DeleteExpensePOMs
from tests.poms.finance_tracking.expense.detail import ExpenseDetailPOMs
from main.finance_tracking.models import Category, Deposit, Expense
from tests.poms.users.change_password import ChangePasswordPOMs
from tests.poms.finance_tracking.home import FinanceHomePOMs
from selenium.webdriver.edge.webdriver import WebDriver
from django.test import LiveServerTestCase, TestCase
from tests.poms.users.update import UpdateUserPOMs
from tests.poms.users.register import RegisterPOMs
from tests.poms.users.delete import DeleteUserPOMs
from tests.poms.universal import UniversalPOMs
from django.core.management import call_command
from tests.poms.users.login import LoginPOMs
from django.contrib.auth.models import User
from tests.poms.navbar import NavbarPOMs
from main.users.models import CustomUser
from tests.poms.home import HomePOMs
from behave.runner import Context

class HostTest(LiveServerTestCase, TestCase):
    # Setup for webdriver and POM files before selenium tests
    def before_all(context: Context):
        ## Setup ptest environment
        # base_user1 = User.objects.create_user(username='test1', first_name='first', last_name='last', email='first@last.com', password='pass12345')
        # user1 = CustomUser.objects.create(user=base_user1, phone_number='1-111-222-3333')
        # base_user2 = User.objects.create_user(username='test2', first_name='first', last_name='last', email='first@last.com', password='pass12345')
        # user2 = CustomUser.objects.create(user=base_user2, phone_number='1-111-222-3333')
        # base_user3 = User.objects.create_user(username='test3', first_name='first', last_name='last', email='first@last.com', password='pass12345')
        # user3 = CustomUser.objects.create(user=base_user3, phone_number='1-111-222-3333')
        # category1 = Category.objects.create(name='test1', user=base_user3, group='deposit')
        # category2 = Category.objects.create(name='test2', user=base_user3, group='expense')
        # category3 = Category.objects.create(name='test3', user=base_user3, group='deposit')
        # category4 = Category.objects.create(name='test4', user=base_user3, group='expense')
        # deposit1 = Deposit.objects.create(user=base_user3, category=category3, date='2024-01-12', description='test deposit 1', amount=45.35)
        # expense1 = Expense.objects.create(user=base_user3, category=category3, date='2024-01-12', description='test expense 1', amount=45.35)

        ## Setupp web driver
        context.driver = WebDriver()

        ## register POM files below
        ### home poms
        context.home_poms = HomePOMs(context.driver)

        ### track finances poms
        context.finance_poms = FinanceHomePOMs(context.driver)

        ### users poms
        context.login_poms = LoginPOMs(context.driver)
        context.register_poms = RegisterPOMs(context.driver)
        context.change_password_poms = ChangePasswordPOMs(context.driver)
        context.update_user_poms = UpdateUserPOMs(context.driver)
        context.delete_user_poms = DeleteUserPOMs(context.driver)

        ### category poms
        context.create_category_poms = CreateCategoryPOMs(context.driver)
        context.update_category_poms = UpdateCategoryPOMs(context.driver)
        context.delete_category_poms = DeleteCategoryPOMs(context.driver)

        ### deposit poms
        context.manage_deposits_poms = ManageDepositsPOMs(context.driver)
        context.create_deposit_poms = CreateDepositPOMs(context.driver)
        context.update_deposit_poms = UpdateDepositPOMs(context.driver)
        context.delete_deposit_poms = DeleteDepositPOMs(context.driver)
        context.deposit_detail_poms = DepositDetailPOMs(context.driver)

        ### expense poms
        context.manage_expenses_poms = ManageExpensesPOMs(context.driver)
        context.create_expense_poms = CreateExpensePOMs(context.driver)
        context.update_expense_poms = UpdateExpensePOMs(context.driver)
        context.delete_expense_poms = DeleteExpensePOMs(context.driver)
        context.expense_detail_poms = ExpenseDetailPOMs(context.driver)

        ### analyze finance poms
        context.analyze_finances_poms = AnalyzeFinancesPOMs(context.driver)

        ### navigation poms
        context.navbar_poms = NavbarPOMs(context.driver)

        ### universal poms
        context.universal_poms = UniversalPOMs(context.driver)

        context.driver.implicitly_wait(1)

    # Cleanup for webdriver after selenium tests
    def after_all(context: Context):
        ## Close webdriver
        context.driver.close()

        ## Clean up test environment
        ### Delete all objects
        # User.objects.all().delete()
        # CustomUser.objects.all().delete()
        # Category.objects.all().delete()
        # Deposit.objects.all().delete()
        # Expense.objects.all().delete()

        # ### Reset ID sequence for each model
        # call_command('sqlsequencereset', 'auth', 'users', 'main_users_customuser', 'main_finance_tracking_category', 'main_finance_tracking_deposit', 'main_finance_tracking_expense', interactive=False)
