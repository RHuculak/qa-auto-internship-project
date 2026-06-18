from pages.base_page import Page
from pages.main_menu_page import MainMenuPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.contact_us_page import ContactPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_us_page = ContactPage(driver)
