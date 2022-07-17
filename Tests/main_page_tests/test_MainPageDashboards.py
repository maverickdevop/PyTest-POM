import time
import allure
import pytest
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.login_page.LoginPage import LoginPage
from Pages.main_page.MainPage import MainPage
from Tests.test_base import BaseTest


class Test_MainPageProjectDashboards(BaseTest):

    """ Authorize  """
    @allure.description("Залогинемся в Dataforce")
    def test_login_to_site(self):
        self.driver.get(TestData.BASE_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_btn_click()
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    """ Click on menu item  """
    @allure.description("Проверка наличия и клика на пункт меню 'Сводная' в Dataforce")
    def test_do_menu_item_click(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_menu_item()

    """ Check H2 title on page  """
    @allure.description("Проверка title-H2 страницы 'Сводная'")
    def test_check_h2_text_page(self):
        self.mainPage = MainPage(self.driver)
        h2 = self.mainPage.get_page_h2()
        print("Page name in H2 title:", h2)

        assert h2 == TestData.H2_MAIN, f"Not correct H2 Title on main page"

    """ Check dashboards block available on page  """
    @allure.description("Проверка наличия дашбордов на странице 'Сводная'  в Dataforce")
    def test_check_dashboards_exist(self):
        self.mainPage = MainPage(self.driver)
        dashboard = self.mainPage.is_dashboard_block_exist()

        assert dashboard is True, f"Dashboard not located on main page"

    """ Check region selector available on page  """
    @allure.description("Проверка наличия селектора региона на странице 'Сводная' в дашбордах")
    def test_select_region(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.go_test_project_url()
        self.mainPage.click_on_region()
        self.mainPage.select_region()

    """ Check region selet and validate selected region with expected var in the tab  """
    @allure.description("Проверка выбора региона Москва из списка в 'Сводная' в дашбордах")
    def test_assert_selected_region(self):
        self.mainPage = MainPage(self.driver)
        selected_region = self.mainPage.selected_region()
        print("Selected region in tab:", selected_region, "Query param after region select:", self.mainPage.current_url())

        assert selected_region == TestData.REGION and\
               'region_id=213' in self.mainPage.current_url()

    """ Check region delete and validate selected region disappeared from the region tab  """
    @allure.description("Проверка удаления региона на странице 'Сводная' в дашбордах")
    def test_delete_region(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.del_region()
        selected_region = self.mainPage.selected_region()

        assert TestData.REGION not in selected_region and\
               'region_id=213' not in self.mainPage.current_url(), f'Region not deleted from selector'

    """ Check data-source selector available on page  """
    @allure.description("Проверка наличия селектора источника на странице 'Сводная' в дашбордах")
    def test_select_source(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_source()
        self.mainPage.select_source()

    """ Check data-source selet and validate selected source with expected var in the tab  """
    @allure.description("Проверка выбора источника из списка в 'Сводная' в дашбордах")
    def test_assert_selected_source(self):
        self.mainPage = MainPage(self.driver)
        selected_source = self.mainPage.selected_source()
        print("Selected source in tab:", selected_source,
              "Query param after source select:", self.mainPage.current_url())

        assert selected_source == TestData.SOURCE and\
               'source=google&medium=organic' in self.mainPage.current_url()

    """ Check source delete and validate selected source disappeared from the source tab  """
    @allure.description("Проверка удаления источника на странице 'Сводная' в дашбордах")
    def test_delete_source(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.del_source()
        selected_source = self.mainPage.selected_source()

        assert TestData.SOURCE not in selected_source and\
               'source=google&medium=organic' not in self.mainPage.current_url(), f'Source not deleted from selector'

    """ Validate all types of source are in dropdown list """
    @allure.description("Проверка выбора всех типов источников ")
    def test_select_sources(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_source()
        items = self.mainPage.get_source_count()
        print("Nums of sources in list:", items)

        assert items == 4, f"Get not expected nums of sources"

    """ Check device selector available on page and select both """
    @allure.description("Проверка наличия селектора выбора устройства на странице 'Сводная' в дашбордах")
    def test_select_device(self):
        # Select Desktop
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_device()
        self.mainPage.select_device()
        selected_device = self.mainPage.selected_device()
        print("Selected device in tab:", selected_device, "Query param after device select:",
              self.mainPage.current_url())

        assert selected_device == TestData.DEVICE and\
               'is_mobile=0' in self.mainPage.current_url(), f"Desktop device not selected"

        # Select Mobile
        self.mainPage.click_on_device()
        self.mainPage.select_device_2()

        selected_device = self.mainPage.selected_device()
        print("Selected device in tab:", selected_device, "Query param after device select:",
              self.mainPage.current_url())

        assert selected_device == TestData.DEVICE_2 and\
               'is_mobile=1' in self.mainPage.current_url(), f"Mobile device not selected"

    """ Check device delete and validate selected device disappeared from the device tab  """
    @allure.description("Проверка удаления устройства на странице 'Сводная' в дашбордах")
    def test_delete_device(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.del_device()
        selected_device = self.mainPage.selected_device()

        assert TestData.DEVICE_2 not in selected_device and\
               'is_mobile' not in self.mainPage.current_url(), f'Device not deleted from selector'

    """ Check segment selector available on page and select 1 segemnt and 2 segments """
    @allure.description("Проверка наличия селектора выбора сегментов на странице 'Сводная' в дашбордах")
    def test_select_segments(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_segments()

        # Select 1st Segment
        self.mainPage.select_segment_1()
        selected_segments = self.mainPage.selected_segments()
        len_1st = self.mainPage.len_selected_segments()
        print("Selected segments after 1 select:", selected_segments, "Nums of selected tab:", len_1st)

        assert selected_segments in TestData.SEGMENT_NAME_1 and\
               len_1st == 1 and "catalog_ids=1655359086" in self.mainPage.current_url(), f"Not correct 1st selected segment"

        # Select 2st Segment
        self.mainPage.select_segment_2()
        selected_segments_2 = self.mainPage.selected_multisegments()
        len_2st = self.mainPage.len_selected_segments()
        print("Selected segments after 2 select:", selected_segments_2, "Nums of selected tab:", len_2st)

        assert TestData.SEGMENT_NAME_2 in selected_segments_2 and\
               len_2st == 2 and "catalog_ids=3840176013" in self.mainPage.current_url(), f"Not correct 2nd selected segment"

    """ Check 1 segment delete and validate selected segemnt disappeared from the segemnt tab  """
    """ Check 2nd segment delete and validate all segemnts are disappeared from the segemnt tab  """
    @allure.description("Проверка удаления сегментов на странице 'Сводная' в дашбордах")
    def test_delete_segments(self):
        self.mainPage = MainPage(self.driver)

        # Delete 1 segment
        self.mainPage.del_1_segment()
        len_after_del = self.mainPage.len_selected_segments()
        assert len_after_del == 1, f"Not correct delete 1 segment / Segment not deleted"

        # Delete all segment
        self.mainPage.del_all_segment()
        assert "catalog_ids" not in self.mainPage.current_url(), f"Not correct delete all segment / Segments not deleted"