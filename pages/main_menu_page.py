from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainMenuPage(Page):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[href*="/settings"][class*="settings-link"]')
    # SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a[class=settings-link]')
    MAIN_MENU_BUTTON = (By.CSS_SELECTOR, 'a[href*="/main-menu"]')
    def navigate_to_settings(self):
        self.wait_until_clickable(*self.MAIN_MENU_BUTTON)
        self.click(*self.MAIN_MENU_BUTTON)
        self.wait_until_clickable(*self.SETTINGS_BUTTON)
        self.scroll_to(*self.SETTINGS_BUTTON)
        self.click(*self.SETTINGS_BUTTON)
        sleep(2)