import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options
from Config import config

""" Create fixture for driver initiate """
""" Use --- type for run test with specifically driver (Chrome/Firefox)"""


@pytest.fixture(params=["firefox","chrome"], scope="class")
def init_driver(request):

    global browser

    if request.param == "chrome":
        browser = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == "firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    else:
        print("Set available driver")

    request.cls.driver = browser
    browser.maximize_window()
    yield
    browser.close()

""" Driver Options for Google Chrome """
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('-start-maximized')
    options.add_argument('--window-size=1200,700')
    return options

""" Get Chrome driver with options """
@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = TestData.BASE_URL

    if request.cls is not None:
        request.csl.driver = driver
    driver.get(url)
    yield  driver
    driver.quit()

