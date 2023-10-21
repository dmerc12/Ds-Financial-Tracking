from behave import when

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
