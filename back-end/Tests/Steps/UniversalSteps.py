from behave import given, then

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')


@then('I should see a toast notification saying {expected_text}')
def step_impl(context, expected_text):
    toast_message = context.universal_poms.toast_notification_text()
    assert expected_text == toast_message
