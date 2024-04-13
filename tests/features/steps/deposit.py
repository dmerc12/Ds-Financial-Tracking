from behave import when

# Steps for create deposit feature file
@when(u'I click the create deposit button')
def step_impl(context):
    context.manage_deposits_poms.click_create_deposit_link()

@when(u'I select {category} in the deposit category select')
def step_impl(context, category):
    context.create_deposit_poms.select_category(category)

@when(u'I input {date} in the deposit date input')
def step_impl(context, date):
    context.create_deposit_poms.enter_date(date)

@when(u'I enter {description} in the deposit description input')
def step_impl(context, description):
    context.create_deposit_poms.enter_description(description)

@when(u'I enter {amount} in the deposit amount input')
def step_impl(context, amount):
    context.create_deposit_poms.enter_amount(amount)

@when(u'I click the create deposit button')
def step_impl(context):
    context.create_deposit_poms.click_create_deposit_button()
