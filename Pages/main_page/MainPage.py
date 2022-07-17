from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import random
from random import random, randrange, randint


class MainPage(BasePage):

    """ Creating test locators on Main page"""
    TITLE_HEADER = (By.XPATH, "//h2[@id='title-secondary']")
    DASHBOARD_FILTERS_BLOCK = (By.XPATH, "//div[@class='dashboard-filters']")
    MENU_ITEM = (By.XPATH, "//a[@class='router-link-exact-active router-link-active aside-item__link router-link-exact-active']")

    """ Creating test locators for test project select """
    SELECTOR_PROJECT = (By.XPATH, "//div[@class='projects']//div[@class='select-bar']")
    INPUT_PROJECT_NAME = (By.XPATH, "//input[@placeholder='Поиск...']")
    SELECT_FOUND_PROJECT = (By.XPATH, "//*[contains(text(),'proskater.ru DF')]")
    PROJECT_TAB = (By.XPATH, "//div[@class='projects__value']")
    PROJECT_IMG = (By.XPATH, "//span[@class='select-item__data']/img")

    """ Creating test locators for test dashboards """

    """ Region xpath """
    REGION_SELECTOR = (By.XPATH, '//*[@id="filters_region"]/div')
    SELECT_REGION = (By.XPATH, "//ul[@class='select-drop-options']/li/span[text()='Москва']")
    REGION_TAB = (By.XPATH, '//*[@id="filters_region"]/div/div')
    REGION_DEL = (By.XPATH, '//*[@id="filters_region"]/div/button')

    """ Source xpath """
    SOURCE_SELECTOR = (By.XPATH, '//*[@id="filters_source"]/div')
    SELECT_SOURCE = (By.XPATH, "//ul[@class='select-drop-options']/li/span[text()='Google/organic']")
    SOURCE_TAB = (By.XPATH, '//*[@id="filters_source"]/div/div')
    SOURCE_LIST = (By.XPATH, "//ul[@class='select-drop-options']/li")
    SOURCE_DEL = (By.XPATH, '//*[@id="filters_source"]/div/button')

    """ Device xpath """
    DEVICE_SELECTOR = (By.XPATH, '//*[@id="filters_device"]/div')
    SELECT_DEVICE = (By.XPATH, "//ul[@class='select-drop-options']/li/span[text()='Desktop']")
    SELECT_DEVICE_2 = (By.XPATH, "//ul[@class='select-drop-options']/li/span[text()='Mobile']")
    DEVICE_TAB = (By.XPATH, '//*[@id="filters_device"]/div/div')
    DEVICE_DEL = (By.XPATH, '//*[@id="filters_device"]/div/button')

    """ Segments xpath """
    SEGMENT_SELECTOR = (By.XPATH, '//*[@id="select_segments"]/div/span')
    SEGMENT_1 = (By.XPATH, '//*[@id="select_segments_list"]/li[34]/div/div[2]')
    SEGMENT_2 = (By.XPATH, '//*[@id="select_segments_list"]/li[35]/div/div[2]')
    SEGMENT_TAB = (By.XPATH, '//*[@id="select_segments"]/div/div/div/div')
    TAB_SEGMENT = (By.XPATH, '//div[@class="multiselect-bar-tab"]')
    MULTISEGMENT_TAB = (By.XPATH, '//*[@id="select_segments"]/div/div/div[@class="multiselect-bar-tabs__case"]')
    DEL_SEGMENT = (By.XPATH, '//*[@id="select_segments"]/div/div/div/div[1]/div')
    DEL_ALL_SEGMENT = (By.XPATH, '//*[@id="select_segments"]/div/button')

    """ Functions init driver for pages """
    def __init__(self, driver):
        super().__init__(driver)

    """ Main page functions """
    def get_title_main_page(self, title):
        return self.get_title(title)

    def get_page_h2(self):
        return self.get_element_text(self.TITLE_HEADER)

    def is_dashboard_block_exist(self):
        return self.is_visible(self.DASHBOARD_FILTERS_BLOCK)

    def click_on_menu_item(self):
        self.do_clickable(self.MENU_ITEM)

    def get_url(self):
        return self.current_url()

    """ Functions with project selection """

    """ Project """
    def click_on_project_selector(self):
        self.do_click(self.SELECTOR_PROJECT)

    def click_on_random_project(self):
        landom_li = random.randint(0, 10)
        self.do_click((By.XPATH, "//ul[@class='select-drop-options']/li["+landom_li"]"))

    def do_search_project(self, project_name):
        self.do_click(self.SELECTOR_PROJECT)
        self.do_send_keys(self.INPUT_PROJECT_NAME, project_name)
        self.do_click(self.SELECT_FOUND_PROJECT)

    def get_project_value_tab(self):
        return self.get_element_innertext(self.PROJECT_TAB)

    def get_project_img(self):
        return self.get_element_src(self.PROJECT_IMG)

    """ Functions with dashboards """
    
    """ Region """
    def click_on_region(self):
        self.do_click(self.REGION_SELECTOR)

    def select_region(self):
        self.do_click(self.SELECT_REGION)

    def selected_region(self):
        return self.get_element_text(self.REGION_TAB)

    def del_region(self):
        self.do_click(self.REGION_DEL)

    """ Source """
    def click_on_source(self):
        self.do_click(self.SOURCE_SELECTOR)

    def select_source(self):
        self.do_click(self.SELECT_SOURCE)

    def selected_source(self):
        return self.get_element_text(self.SOURCE_TAB)

    def del_source(self):
        self.do_click(self.SOURCE_DEL)

    def get_source_count(self):
        return self.get_count(self.SOURCE_LIST)

    """ Device """
    def click_on_device(self):
        self.do_click(self.DEVICE_SELECTOR)

    def select_device(self):
        self.do_click(self.SELECT_DEVICE)

    def select_device_2(self):
        self.do_click(self.SELECT_DEVICE_2)

    def selected_device(self):
        return self.get_element_text(self.DEVICE_TAB)

    def del_device(self):
        self.do_click(self.DEVICE_DEL)

    """ Segments """
    def click_on_segments(self):
        self.do_click(self.SEGMENT_SELECTOR)

    def select_segment_1(self):
        self.do_click(self.SEGMENT_1)

    def select_segment_2(self):
        self.do_click(self.SEGMENT_2)

    def selected_segments(self):
        return self.get_element_innertext(self.SEGMENT_TAB)

    def len_selected_segments(self):
        return self.get_count(self.TAB_SEGMENT)

    def selected_multisegments(self):
        return self.get_element_innertext(self.MULTISEGMENT_TAB)

    def del_1_segment(self):
        self.do_click(self.DEL_SEGMENT)

    def del_all_segment(self):
        self.do_click(self.DEL_ALL_SEGMENT)