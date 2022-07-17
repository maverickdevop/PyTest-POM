import allure
from Config.config import TestData
from Pages.login_page.LoginPage import LoginPage
from Pages.main_page.MainPage import MainPage
from Tests.test_base import BaseTest


class Test_MainPageProjectSelect(BaseTest):

    """ Authorize  """
    @allure.description("Залогинемся в Dataforce")
    def test_login_to_site(self):
        self.driver.get(TestData.BASE_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_btn_click()
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    """ Click on project selector and check img src in projects list  """
    @allure.description("Поиск и клик на селектор выбора проекта в Dataforce / Проверка лого проекта")
    def test_project_selector_click(self):
        self.searchProject = MainPage(self.driver)
        self.searchProject.click_on_project_selector()
        img_project = self.searchProject.get_project_img()
        print("Img source of project:", img_project)

        assert img_project, f'Project not include image logo!'

    """ Select random project from list with random function """
    """ import random
        from random import randint
        def click_on_random_project(self):
        landom_li = random.randint(0, 10)
        self.do_click((By.XPATH, "//ul[@class='select-drop-options']/li["+landom_li"]"))
    """

    @allure.description("Выбор рандомного проекта из выпадающего списка в Dataforce")
    def test_project_list_select(self):
        self.searchProject = MainPage(self.driver)
        self.searchProject.click_on_random_project()
        len_tab = self.searchProject.get_project_value_tab()
        print("Lenght of project tab:", len(len_tab), "symbols")

        assert len(len_tab) > 0, f'Selector of project is empty!'

    """ Find project in project selecor """
    @allure.description("Поиск по проекту и выбор найденного проекта в Dataforce")
    def test_project_search_select(self):
        self.searchProject = MainPage(self.driver)
        self.searchProject.do_search_project(TestData.PROJECT_NAME)

    """ Validate selected project with expected project name """
    @allure.description("Проверка что именно нужный проект в селекторе проектов в Dataforce")
    def test_project_tab_assert(self):
        self.searchProject = MainPage(self.driver)
        project_in_tab = self.searchProject.get_project_value_tab()
        url = self.searchProject.current_url()
        print("Selected project in Project-tab:", project_in_tab, "URL after project select:", url)

        assert project_in_tab == TestData.PROJECT_NAME and TestData.URL_PROJECT in url, f'Selected project is not matched with expected project!'
