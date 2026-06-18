from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome()
    context.driver = webdriver.Firefox()

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = Options()
    # context.driver = webdriver.Chrome(service=service, options=options)

    # Headless mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("--incognito")
    # context.driver = webdriver.Chrome(options=options)
    #



    # Browserstack config
    # bs_user = 'ryan_LUZehz'
    # bs_key = 'zqhu5YxuV1f37K38T63h'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options  = {
    #     "os": "Windows",
    #     "osVersion": "10",
    #     "browserName": "Chrome",
    #     "browserVersion": "120.0",
    #     'sessionName': scenario_name
    # }
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Tahoe",
    #     "browserName": "Chrome",
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #

    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario}')
    browser_init(context, scenario.name)

def before_step(context, step):
    logger.info(f'Started step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    context.driver.quit()
