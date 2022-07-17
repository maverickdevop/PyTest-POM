import allure

from Config.config import TestData
from Pages.login_page.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    """ Write test-cases here """
    @allure.description("Переход на базовый URL Dataforce")
    def test_get_to_site(self):
        self.driver.get(TestData.BASE_URL)

    """ Check for correct title """
    @allure.description("Проверка title-лендинга Dataforce")
    def test_landing_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title_landing = self.loginPage.get_landing_page_title(TestData.LANDING_PAGE_TITLE)
        print('Landing site title:', title_landing)
        assert title_landing == TestData.LANDING_PAGE_TITLE

    """ Check login button click on header """
    @allure.description("Проверка наличия и клика на кнопку логина")
    def test_click_login_button(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_btn_click()

    """ Check login correct working """
    @allure.description("Проверка логина на сайт Dataforce")
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    """ Check valid title after login on main page """
    @allure.description("Проверка валидного title 'Сводная' страницы после авторизации в Dataforce")
    def test_login_successful(self):
        self.loginPage = LoginPage(self.driver)
        email_header = self.loginPage.get_desktop_title(TestData.HOME_PAGE_TITLE)
        print('Desktop site title:', email_header)
        assert email_header == TestData.HOME_PAGE_TITLE

    """ Check valid login on profile """
    @allure.description("Проверка валидного email после авторизации")
    def test_user_logged(self):
        self.loginPage = LoginPage(self.driver)
        email_value = self.loginPage.get_email_value()
        print('Logged user is:', email_value)
        assert email_value == TestData.USER_EMAIL_HEADER