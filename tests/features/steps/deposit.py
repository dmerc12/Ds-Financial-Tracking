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

# Steps for update deposit feature file
@when(u'I click deposit ID {id}')
def step_impl(context, id):
    context.manage_deposits_poms.click_deposit_id(id)

@when(u'I click the update deposit navigation button')
def step_impl(context):
    context.deposit_detail_poms.click_update_deposit_link()

@when(u'I click the update deposit button')
def step_impl(context):
    context.update_deposit_poms.click_update_deposit_button()

# Steps for delete deposit feature file
@when(u'I click the delete deposit navigation button')
def step_impl(context):
    context.deposit_detail_poms.click_delete_deposit_link()

@when(u'I click the delete deposit button')
def step_impl(context):
    context.delete_deposit_poms.click_delete_deposit_button()

# Steps for deposit search feature file
@when(u'I click the search tab')
def step_impl(context):
    context.manage_deposits_poms.click_search_toggle()

@when(u'I input {id} in the deposit ID input')
def step_impl(context, id):
    context.manage_deposits_poms.enter_deposit_id_in_search_input(id)
