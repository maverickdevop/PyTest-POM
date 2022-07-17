from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData

""" This class is the parent of all pages """
""" It contains all the generic method and utilities for all the pages """


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def do_click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def go_test_project_url(self):
        self.driver.get(TestData.TEST_PROJECT_URL)

    def do_clickable(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.text

    def get_element_innertext(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute("innerText")

    def get_element_innerhtml(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute("innerHTML")

    def get_element_src(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element.get_attribute("src")

    def is_visible(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

    def current_url(self):
        return self.driver.current_url

    def get_driver_title(self):
        return self.driver.title

    def get_count(self, by_locator):
        return len(self.wait.until(EC.presence_of_all_elements_located(by_locator)))