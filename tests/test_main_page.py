import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.lk_page import LKPage
from pages.main_page import MainPage
from data.urls import Urls
from conftest import *


class TestMainPage:
    @allure.title('Проверка перехода в Ленту заказов по кнопке в шапке лендинга')
    def test_go_to_order_list(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.go_to_order_list()
        assert mainpage.get_current_url() == Urls.URL_FEED

    @allure.title('Проверка перехода в Конструктор по кнопке в шапке лендинга')
    def test_go_to_constructor(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.go_to_lk()
        mainpage.go_to_constructor()
        assert mainpage.get_current_url() == Urls.URL

    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    def test_get_ingredient_popup(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.click_ingredient()
        assert mainpage.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == True

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_close_ingredient_popup(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.click_ingredient()
        mainpage.close_popup()
        assert mainpage.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.add_bun_to_order_basket()
        assert mainpage.get_counter_of_ingredients() == '2'

    @allure.title('Проверка успешного создания заказа')
    def test_successful_order(self, driver, user_sign_in):
        mainpage = MainPage(driver)
        mainpage.add_bun_to_order_basket()
        mainpage.click_order_button()
        mainpage.wait_until_element_visibility(20, MainPageLocators.ORDER_NUMBER)
        assert mainpage.find_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True