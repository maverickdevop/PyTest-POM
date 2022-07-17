import time
import allure

from Config.config import TestData
from Pages.login_page.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    """ Write test-cases here """
    @allure.description("Переход на базовый URL Dataforce")
    def test_get_to_site(self):
        self.driver.get(TestData.BASE_URL)

    """ Check login button click on header """
    @allure.description("Проверка наличия и клика на кнопку логина")
    def test_click_login_button(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_btn_click()

    """ Check empty login input """
    @allure.description("Проверка ввода пустого логина")
    def test_void_login_data_login(self):

        while True:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME_VOID, TestData.PASSWORD)
            void_user_msg_error = self.loginPage.get_auth_error()

            print('Auth error incase empty user  is:', void_user_msg_error)
            assert TestData.VOID_LOGIN_ERROR in void_user_msg_error
            break

    """ Check empty password input """
    @allure.description("Проверка ввода пустого пароля")
    def test_void_password_data_login(self):

        self.driver.get(TestData.BASE_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_btn_click()

        while True:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD_VOID)
            void_password_msg_error = self.loginPage.get_auth_error()

            print('Auth error incase empty password  is:', void_password_msg_error)
            assert TestData.VOID_PASSWORD in void_password_msg_error
            break