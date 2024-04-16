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

# Steps for login feature file
@when(u'I input {username} in the login username input')
def step_impl(context, username):
    context.login_poms.enter_username_input(username)

@when(u'I input {password} in the login password input')
def step_impl(context, password):
    context.login_poms.enter_password_input(password)

@when(u'I click the login button')
def step_impl(context):
    context.login_poms.click_login_button()

# Steps for update feature file
@when(u'I click the manage information button')
def step_impl(context):
    context.home_poms.click_manage_information_button()

@when(u'I enter {new_username} in the update username input')
def step_impl(context, new_username):
    context.update_user_poms.enter_username_input(new_username)

@when(u'I enter {first_name} in the update first name input')
def step_impl(context, first_name):
    context.update_user_poms.enter_first_name_input(first_name)

@when(u'I enter {last_name} in the update last name input')
def step_impl(context, last_name):
    context.update_user_poms.enter_last_name_input(last_name)

@when(u'I enter {email} in the update email input')
def step_impl(context, email):
    context.update_user_poms.enter_email_input(email)

@when(u'I enter {phone_number} in the update phone number input')
def step_impl(context, phone_number):
    context.update_user_poms.enter_phone_number_input(phone_number)

@when(u'I click the update information button')
def step_impl(context):
    context.update_user_poms.click_update_user_button()

# Steps for change password feature
@when(u'I click the change password navigation button')
def step_impl(context):
    context.update_user_poms.click_change_password_link()

@when(u'I enter {new_password1} in the new password 1 input')
def step_impl(context, new_password1):
    context.change_password_poms.enter_password1_input(new_password1)

@when(u'I enter {new_password2} in the new password 2 input')
def step_impl(context, new_password2):
    context.change_password_poms.enter_password2_input(new_password2)

@when(u'I click the change password button')
def step_impl(context):
    context.change_password_poms.click_change_password_button()

# Steps for delete user feature
@when(u'I click the delete user navigation button')
def step_impl(context):
    context.update_user_poms.click_delete_user_link()

@when(u'I click the delete user button')
def step_impl(context):
    context.delete_user_poms.click_delete_user_button()
