from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainMenuPage(Page):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[href*="/settings"]')
    def navigate_to_settings(self):
        self.wait_until_clickable(*self.SETTINGS_BUTTON)
        self.click(*self.SETTINGS_BUTTON)
        sleep(3)