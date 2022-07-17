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

    """ Authorize  """
    @allure.description("Авторизация на Dataforce")
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    """ Click to logout and validate  """
    @allure.description("Проверка наличия кнопки разлогина в шапке / Совершение разлогина/ Проверка title разлогина")
    def test_logout(self):
        # Logout
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout_click()

        # Assert URL / And title login after logout
        print("URL after logout:", self.loginPage.current_url())
        title_login = self.loginPage.get_driver_title()

        print("Title login after logout:", title_login)
        assert 'dataforce.io/login' in self.loginPage.current_url() and title_login == TestData.LOGIN_TITLE