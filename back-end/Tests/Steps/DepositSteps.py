from behave import when

@when(u'I click the manage deposits button in the navigation bar')
def step_impl(context):
    context.deposit_poms.click_manage_deposits_nav_button()


@when(u'I click the manage deposits button')
def step_impl(context):
    context.deposit_poms.click_manage_deposits_button()


@when(u'I click the create deposit modal')
def step_impl(context):
    context.deposit_poms.click_create_deposit_modal()


@when(u'I select {category_id} the create deposit category input')
def step_impl(context, category_id):
    context.deposit_poms.select_create_deposit_category_id(category_id)


@when(u'I input {date} in the create deposit date input')
def step_impl(context, date):
    context.deposit_poms.input_create_deposit_date(date)


@when(u'I input {description} in the create deposit description input')
def step_impl(context, description):
    context.deposit_poms.input_create_deposit_description(description)


@when(u'I input {amount} in the create deposit amount input')
def step_impl(context, amount):
    context.deposit_poms.input_create_deposit_amount(amount)


@when(u'I click the create deposit button')
def step_impl(context):
    context.deposit_poms.click_create_deposit_button()


@when(u'I click the update deposit modal on deposit {deposit_id}')
def step_impl(context, deposit_id):
    context.deposit_poms.click_update_deposit_modal(deposit_id)


@when(u'I select {category_id} the update deposit category input')
def step_impl(context, category_id):
    context.deposit_poms.select_update_deposit_cateogry_id(category_id)


@when(u'I input {date} in the update deposit date input')
def step_impl(context, date):
    context.deposit_poms.input_update_deposit_date(date)


@when(u'I input {description} in the update deposit description input')
def step_impl(context, description):
    context.deposit_poms.input_update_deposit_description(description)


@when(u'I input {amount} in the update deposit amount input')
def step_impl(context, amount):
    context.deposit_poms.input_update_deposit_amount(amount)


@when(u'I click the update deposit button')
def step_impl(context):
    context.deposit_poms.click_update_deposit_button()


@when(u'I click the delete deposit modal on deposit {deposit_id}')
def step_impl(context, deposit_id):
    context.deposit_poms.click_delete_deposit_modal(deposit_id)


@when(u'I click the delete deposit button')
def step_impl(context):
    context.deposit_poms.click_delete_deposit_button()
