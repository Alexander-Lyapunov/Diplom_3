import allure
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.step('Нажимаем на заказ в Ленте заказов')
    def click_order(self):
        self.click_element(OrderListPageLocators.ORDER_LINK)

    @allure.step('Получаем общее количество заказов, выполненных за все время')
    def get_all_time_orders_total(self):
        return self.get_element_text(OrderListPageLocators.ORDERS_ALL_TIME)

    @allure.step('Получаем общее количество заказов, выполненных за сегодня')
    def get_today_orders_total(self):
        return self.get_element_text(OrderListPageLocators.ORDERS_TODAY)

    @allure.step('Ищем созданный заказ по номеру среди заказов в работе')
    def get_order_number_in_work(self):
        return self.get_element_text(OrderListPageLocators.ORDER_IN_WORK)