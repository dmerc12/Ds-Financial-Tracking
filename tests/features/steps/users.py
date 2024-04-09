from behave import when

# Steps for register feature file
@when(u'I click on the sign up link')
def step_impl(context):
    context.login_poms.click_register_link()

@when(u'I input {username} in the register username input')
def step_impl(context, username):
    context.register_poms.enter_username_input(username)

@when(u'I input {first_name} in the register first name input')
def step_impl(context, first_name):
    context.register_poms.enter_first_name_input(first_name)

@when(u'I input {last_name} in the register last name input')
def step_impl(context, last_name):
    context.register_poms.enter_last_name_input(last_name)

@when(u'I input {email} in the register email input')
def step_impl(context, email):
    context.register_poms.enter_email_input(email)

@when(u'I input {phone_number} in the register phone number input')
def step_impl(context, phone_number):
    context.register_poms.enter_phone_number_input(phone_number)

@when(u'I input {password} in the register password input')
def step_impl(context, password):
    context.register_poms.enter_password1_input(password)

@when(u'I input {confirm_password} in the register password confirmation input')
def step_impl(context, confirm_password):
    context.register_poms.enter_password2_input(confirm_password)

@when(u'I click the registser button')
def step_impl(context):
    context.register_poms.click_register_button()

