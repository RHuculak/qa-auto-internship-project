from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, end_url=''):
        self.driver.get(f'https://soft.reelly.io//{end_url}')
        sleep(2)

    def find_element(self, *locator):
        logger.info(f'Finding element by locator: {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Finding elements by locator: {locator}')
        return self.driver.find_elements(*locator)

    def wait_until_clickable(self, *locator):
        logger.info(f'Waiting until {locator} is clickable')
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def click(self, *locator):
        logger.info(f'Attempting to click element: {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Setting text value for {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def verify_url(self, url):
        logger.info(f'Verifying url: {url}')
        sleep(6)
        assert url in self.driver.current_url

    def scroll_to(self, *element):
        ele = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ele)
        sleep(2)