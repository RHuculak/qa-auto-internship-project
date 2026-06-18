from pages.base_page import Page
from selenium.webdriver.common.by import By

class ContactPage(Page):
    WHATSAPP_BUTTON = (By.CSS_SELECTOR, 'a[class*="whatsapp"]')
    def whatsapp_clickable(self):
        self.wait_until_clickable(*self.WHATSAPP_BUTTON)