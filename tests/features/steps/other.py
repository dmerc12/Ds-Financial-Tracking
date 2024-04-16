from behave import when

# Steps for back feature file
@when(u'I click the back button')
def step_impl(context):
    context.universal_poms.click_back_button()

# Steps for navbar feature file
@when(u'I click the home tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_home_tab()

@when(u'I click the manage information tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_manage_info_tab()

@when(u'I click the track finances dropdown in the navbar')
def step_impl(context):
    context.navbar_poms.click_track_finances_toggle()

@when(u'I click the manage deposits tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_deposit_home_tab()

@when(u'I click the manage expenses tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_expense_home_tab()

@when(u'I click the view finances tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_view_finances_tab()

@when(u'I click the analyze finances tab in the navbar')
def step_impl(context):
    context.navbar_poms.click_analyze_finances_tab()

@when(u'I click the logout button in the navbar')
def step_impl(context):
    context.navbar_pomss.click_logout_tab()

# Steps for navigation feature file
@when(u'I click the view finances button')
def step_impl(context):
    context.finance_poms.view_finances_link()

# Steps for search feature file
@when(u'I click the analyze finances buttton')
def step_impl(context):
    context.finance_poms.analyze_finances_link()

@when(u'I input {start_date} in the start input')
def step_impl(context, start_date):
    context.manage_deposits_poms.enter_start_date_in_search_input(start_date)

@when(u'I input {end_date} in the end date input')
def step_impl(context, end_date):
    context.manage_deposits_poms.enter_end_date_in_search_input(end_date)

@when(u'I click the search button')
def step_impl(context):
    context.manage_deposits_poms.click_search_button()
