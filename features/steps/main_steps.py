from behave import given, when, then

MAIN_PAGE = "main"

@given("Open Reelly {path} page")
def open_target_page(context, path):
    if path == MAIN_PAGE:
        path = ""
    context.app.page.open_url(path)

@then("User can log in")
def user_can_log_in(context):
    context.app.main_page.login()