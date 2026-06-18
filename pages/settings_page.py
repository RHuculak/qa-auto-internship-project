from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SettingsPage(Page):
    CONTACT_BUTTON = (By.CSS_SELECTOR, 'a[href*="/contact-us"]')
    def contact_us(self):
        self.scroll_to(*self.CONTACT_BUTTON)
        sleep(1)
        self.wait_until_clickable(*self.CONTACT_BUTTON)
        self.click(*self.CONTACT_BUTTON)
        sleep(3)