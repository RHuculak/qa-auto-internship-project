from behave import given, when, then

@then('User can click contact us')
def click_contact_us(context):
    context.app.settings_page.contact_us()