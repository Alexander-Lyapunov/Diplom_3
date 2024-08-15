import allure
from locators.auth_page_locators import AuthPageLocators
from pages.lk_page import LKPage
from data.urls import Urls
from conftest import *


class TestAccountPage:
    @allure.title('Проверка перехода по кнопке Личный кабинет')
    def test_go_to_account_from_header(self, driver, user_sign_in):
        lkpage = LKPage(driver)
        lkpage.click_account_button_with_auth()
        assert lkpage.get_current_url() == Urls.URL_ACCOUNT

    @allure.title('Проверка перехода в раздел История заказов')
    def test_go_to_history_order(self, driver, user_sign_in):
        lkpage = LKPage(driver)
        lkpage.click_account_button_with_auth()
        lkpage.go_to_history_order_list()
        assert lkpage.get_current_url() == Urls.URL_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_user_logout(self, driver, user_sign_in):
        lkpage = LKPage(driver)
        lkpage.click_account_button_with_auth()
        lkpage.click_logout_button()
        assert lkpage.get_element_text(AuthPageLocators.BUTTON_ENTER) == 'Войти'