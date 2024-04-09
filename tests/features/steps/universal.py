from behave import given, then

@given(u'I am on the login page')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/users/login/')

@then(u'I should be on the a page with the title {title}')
def step_impl(context, title):
    assert context.driver.title == title
