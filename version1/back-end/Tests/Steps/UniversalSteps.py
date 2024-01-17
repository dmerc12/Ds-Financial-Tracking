from behave import given, when, then

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get('http://localhost:5173/')


@when(u'I click the home button in the navigation bar')
def step_impl(context):
    context.universal_poms.click_home_nav_button()


@then(u'I am on a page with the tite {title}')
def step_impl(context, title):
    assert context.driver.title == title


@then('I should see a toast notification saying {expected_text}')
def step_impl(context, expected_text):
    toast_message = context.universal_poms.toast_notification_text()
    assert expected_text == toast_message
