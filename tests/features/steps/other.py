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
