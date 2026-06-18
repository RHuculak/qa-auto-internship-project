from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

class MainPage(Page):
    username = os.getenv('REELLY_USERNAME')
    password = os.getenv('REELLY_PASSWORD')
    USERNAME_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
    def open_main(self):
        self.open_url()
    def login(self):
        self.input_text(self.username, *self.USERNAME_INPUT)
        self.input_text(self.password, *self.PASSWORD_INPUT)
        sleep(3)
        self.wait_until_clickable(*self.LOGIN_BUTTON)
        self.click(*self.LOGIN_BUTTON)
        sleep(10)

