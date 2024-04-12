from behave import when

# Steps for create category feature file
@when(u'I click track finances button')
def step_impl(context):
    context.home_poms.click_track_finances_button()

@when(u'I click the create deposit category button')
def step_impl(context):
    context.manage_deposits_poms.click_create_category_link()

@when(u'I click the create expense category button')
def step_impl(context):
    context.manage_expenses_poms.click_create_category_link()

@when(u'I click the manage deposits buttton')
def step_impl(context):
    context.finance_poms.click_manage_deposits_link()

@when(u'I click the manage expenses buttton')
def step_impl(context):
    context.finance_poms.click_manage_expenses_link()

@when(u'I enter {name} in the category name input')
def step_impl(context, name):
    context.create_category_poms.enter_name_input(name)

@when(u'I enter the create category button')
def step_impl(context):
    context.create_category_poms.click_create_category_button()

# Steps for update category feature file
@when(u'I click the update deposit category button')
def step_impl(context):
    context.manage_deposits_poms.click_update_category_link()

@when(u'I click the update expense category button')
def step_impl(context):
    context.manage_expenses_poms.click_update_category_link()

@when(u'I enter the update category button')
def step_impl(context):
    context.update_category_poms.click_update_category_button()

# Steps for delete category feature file
@when(u'I click the delete deposit category button')
def step_impl(context):
    context.manage_deposits_poms.click_delete_category_toggle()

@when(u'I click the delete expense category button')
def step_impl(context):
    context.manage_expenses_poms.click_delete_category_toggle()

@when(u'I click the delete category button')
def step_impl(context):
    context.delete_category_poms.click_delete_category_button()