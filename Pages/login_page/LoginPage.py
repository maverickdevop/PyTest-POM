import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.main_page.MainPage import MainPage


class LoginPage(BasePage):

    """ Creating test locators on login_tests page"""
    ENTER_BUTTON_HEADER = (By.XPATH, "//a[contains(text(),'войти')]")
    EMAIL = (By.XPATH, "//input[@placeholder='Ваш логин']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Введите новый пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_ASSERT = (By.XPATH, "//button[@class='user__button']/span")

    """ Error locator """
    AUTH_ERROR = (By.XPATH, "//div[@class='notification-text']/div[@class='notification-title']")

    """ User button locators """
    USER_BTN = (By.XPATH, "//button[@class='user__button']")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Выйти')]")

    """ Constructor of the page class """
    def __init__(self, driver):
        super().__init__(driver)

    """ Page actions for Login page """
    """ This is used to get page title """

    def get_landing_page_title(self, title):
        return self.get_title(title)

    """ This is used to find and click login_tests button """
    def do_login_btn_click(self):
        self.do_click(self.ENTER_BUTTON_HEADER)

    """ This is used to login_tests to app """
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return MainPage(self.driver)

    """ Get title of page after login on page """
    def get_desktop_title(self, title):
        return self.get_title(title)

    """ Get email value after login """
    def get_email_value(self):
        if self.is_visible(self.LOGIN_ASSERT):
            return self.get_element_text(self.LOGIN_ASSERT)

    """ Get notifications error(incase wrong inputted data) """
    def get_auth_error(self):
        return self.get_element_innertext(self.AUTH_ERROR)

    """ This is used to click user button/logout """
    def do_logout_click(self):
        self.do_click(self.USER_BTN)
        self.do_click(self.LOGOUT_BTN)