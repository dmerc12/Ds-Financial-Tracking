from behave import when

# Steps for create expense feature file
@when(u'I click the create expense button')
def step_impl(context):
    context.manage_expenses_poms.click_create_expense_link()

@when(u'I select {category} in the expense category select')
def step_impl(context, category):
    context.create_expense_poms.select_category(category)

@when(u'I input {date} in the expense date input')
def step_impl(context, date):
    context.create_expense_poms.enter_date(date)

@when(u'I enter {description} in the expense description input')
def step_impl(context, description):
    context.create_expense_poms.enter_description(description)

@when(u'I enter {amount} in the expense amount input')
def step_impl(context, amount):
    context.create_expense_poms.enter_amount(amount)

@when(u'I click the create expense button')
def step_impl(context):
    context.create_expense_poms.click_create_expense_button()

# Steps for update expense feature file
@when(u'I click expense ID {id}')
def step_impl(context, id):
    context.manage_expenses_poms.click_expense_id(id)

@when(u'I click the update expense navigation button')
def step_impl(context):
    context.expense_detail_poms.click_update_expense_link()

@when(u'I click the update expense button')
def step_impl(context):
    context.update_expense_poms.click_update_expense_button()

# Steps for delete expense feature file
@when(u'I click the delete expense navigation button')
def step_impl(context):
    context.expense_detail_poms.click_delete_expense_link()

@when(u'I click the delete expense button')
def step_impl(context):
    context.delete_expense_poms.click_delete_expense_button()

# Steps for expense search feature file
@when(u'I click the search tab')
def step_impl(context):
    context.manage_expenses_poms.click_search_toggle()

@when(u'I input {id} in the expense ID input')
def step_impl(context, id):
    context.manage_expenses_poms.enter_expense_id_in_search_input(id)

@when(u'I input {start_date} in the start input')
def step_impl(context, start_date):
    context.manage_expenses_poms.enter_start_date_in_search_input(start_date)

@when(u'I input {end_date} in the end date input')
def step_impl(context, end_date):
    context.manage_expenses_poms.enter_end_date_in_search_input(end_date)

@when(u'I click the search button')
def step_impl(context):
    context.manage_expenses_poms.click_search_button()
