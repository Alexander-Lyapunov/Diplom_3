import allure
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def go_to_lk(self):
        self.click_element(MainPageLocators.LINK_LK)

    @allure.step('Переходим на страницу Лента заказов')
    def go_to_order_list(self):
        self.click_element(MainPageLocators.ORDER_LIST_LINK)
        self.wait_until_element_visibility(20, OrderListPageLocators.ORDER_LIST_TITLE)

    @allure.step('Переходим в Конструктор')
    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)
        self.wait_until_element_visibility(20, MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_BUN)
        self.wait_until_element_visibility(20, MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Закрываем попап')
    def close_popup(self):
        self.wait_until_element_visibility(20, MainPageLocators.CLOSE_BUTTON)
        self.click_element(MainPageLocators.CLOSE_BUTTON)
        self.wait_until_element_invisibility(20, MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Нажимаем на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_until_element_visibility(20, MainPageLocators.ORDER_BUTTON)
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавляем ингредиент "Флюоресцентная булка" в корзину заказа')
    def add_bun_to_order_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.wait_until_element_visibility(20, MainPageLocators.BUN_IN_BASKET)

    @allure.step('Получаем количество добавленного в корзину ингредиента')
    def get_counter_of_ingredients(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создаем заказ и получаем его номер')
    def create_new_order(self):
        self.wait_until_element_visibility(20, MainPageLocators.CONSTRUCTOR_TITLE)
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.click_element(MainPageLocators.ORDER_BUTTON)
        self.wait_until_element_visibility(20, MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_until_element_invisibility(20, MainPageLocators.DEFAULT_ORDER)
        order_number = self.get_element_text(MainPageLocators.ORDER_NUMBER)
        self.click_element(MainPageLocators.CLOSE_BUTTON)
        return order_number