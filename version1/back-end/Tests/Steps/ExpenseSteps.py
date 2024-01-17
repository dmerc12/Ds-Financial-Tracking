from behave import when

@when(u'I click the manage expenses button in the navigation bar')
def step_impl(context):
    context.expense_poms.click_manage_expenses_nav_button()


@when(u'I click the manage expenses button')
def step_impl(context):
    context.expense_poms.click_manage_expenses_button()


@when(u'I click the create expense modal')
def step_impl(context):
    context.expense_poms.click_create_expense_modal()


@when(u'I select {category_id} the create expense category input')
def step_impl(context, category_id):
    context.expense_poms.select_create_expense_category_id(category_id)


@when(u'I input {date} in the create expense date input')
def step_impl(context, date):
    context.expense_poms.input_create_expense_date(date)


@when(u'I input {description} in the create expense description input')
def step_impl(context, description):
    context.expense_poms.input_create_expense_description(description)


@when(u'I input {amount} in the create expense amount input')
def step_impl(context, amount):
    context.expense_poms.input_create_expense_amount(amount)


@when(u'I click the create expense button')
def step_impl(context):
    context.expense_poms.click_create_expense_button()


@when(u'I click the update expense modal on expense {expense_id}')
def step_impl(context, expense_id):
    context.expense_poms.click_update_expense_modal(expense_id)


@when(u'I select {category_id} the update expense category input')
def step_impl(context, category_id):
    context.expense_poms.select_update_expense_category_id(category_id)


@when(u'I input {date} in the update expense date input')
def step_impl(context, date):
    context.expense_poms.input_update_expense_date(date)


@when(u'I input {description} in the update expense description input')
def step_impl(context, description):
    context.expense_poms.input_update_expense_description(description)


@when(u'I input {amount} in the update expense amount input')
def step_impl(context, amount):
    context.expense_poms.input_update_expense_amount(amount)


@when(u'I click the update expense button')
def step_impl(context):
    context.expense_poms.click_update_expense_button()


@when(u'I click the delete expense modal on expense {expense_id}')
def step_impl(context, expense_id):
    context.expense_poms.click_delete_expense_modal(expense_id)


@when(u'I click the delete expense button')
def step_impl(context):
    context.expense_poms.click_delete_expense_button()
