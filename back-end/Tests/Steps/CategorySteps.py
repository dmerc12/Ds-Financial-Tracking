from behave import given, when, then

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')


@when(u'I click the manage categories button')
def step_impl(context):
    context.category_poms.click_manage_categories_button()


@when(u'I click the create category modal')
def step_impl(context):
    context.category_poms.click_create_category_modal()


@when(u'I input {category_name} in the create category name input')
def step_impl(context, category_name):
    context.category_poms.input_create_category_name(category_name)


@when(u'I click the create category button')
def step_impl(context):
    context.category_poms.click_create_category_button()


@then('I should see a toast notification saying {notification_text}')
def step_impl(context, notification_text):
    pass
