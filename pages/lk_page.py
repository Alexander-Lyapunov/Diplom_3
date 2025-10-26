import allure
from data.urls import Urls
from locators.auth_page_locators import AuthPageLocators
from locators.lk_page_locators import LKPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LKPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def click_account_button_with_auth(self):
        self.click_element(MainPageLocators.LINK_LK)
        self.wait_until_element_visibility(20, LKPageLocators.PROFILE_LINK)

    @allure.step('Выходим из аккаунта по кнопке Выход в ЛК')
    def click_logout_button(self):
        self.click_element(LKPageLocators.BUTTON_EXIT)
        self.wait_until_element_visibility(20, AuthPageLocators.BUTTON_ENTER)

    @allure.step('Переходим в Историю заказов по кнопке в ЛК')
    def go_to_history_order_list(self):
        self.click_element(LKPageLocators.ORDER_HISTORY_LINK)
        self.wait_until_url_to_be(20, Urls.URL_HISTORY)

    @allure.step('Получаем список номеров заказов в ленте заказов')
    def get_list_numbers_orders(self):
        list = []
        elements = self.element_list(LKPageLocators.NUMBERS_ORDERS_LIST)
        for element in elements:
            list.append(element.text)
        return list
