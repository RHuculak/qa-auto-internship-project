from behave import given, when, then

@then('User can navigate to settings')
def navigate_to_settings(context):
    context.app.main_menu_page.navigate_to_settings()