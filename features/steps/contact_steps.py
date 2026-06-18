from behave import given, when, then

@when("User is on the {url_segment} page")
def verify_contact_us_page(context, url_segment):
    context.app.page.verify_url(url_segment)

@then("WhatsApp button is clickable")
def verify_whatsapp_button(context):
    context.app.contact_us_page.whatsapp_clickable()