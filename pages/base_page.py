from time import sleep

class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, end_url=''):
        self.driver.get(f'https://www.target.com/{end_url}')
        sleep(2)
