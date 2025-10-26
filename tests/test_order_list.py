import allure
from data.urls import Urls
from locators.order_list_page_locators import OrderListPageLocators
from locators.lk_page_locators import LKPageLocators
from pages.order_list_page import OrderListPage
from pages.main_page import MainPage
from pages.lk_page import LKPage
from conftest import *


class TestOrderListPage:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_get_order_popup(self, driver):
        mainpage = MainPage(driver)
        mainpage.go_to_site(Urls.URL)
        mainpage.go_to_order_list()
        orderpage = OrderListPage(driver)
        orderpage.click_order()
        assert orderpage.find_element(OrderListPageLocators.ORDER_CONTENT).is_displayed() == True

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_find_order_in_list(self, driver, user_sign_in):
        mainpage = MainPage(driver)
        lk_page = LKPage(driver)
        mainpage.create_new_order()
        lk_page.click_account_button_with_auth()
        lk_page.go_to_history_order_list()
        new_user_order = lk_page.get_list_numbers_orders()
        mainpage.go_to_order_list()
        order_list = lk_page.get_list_numbers_orders()
        assert all(order in order_list for order in new_user_order)

    @allure.title('Проверка увеличения счетчика за все время - после создания заказа')
    def test_total_orders_counter(self, driver, user_sign_in):
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.go_to_order_list()
        before_total = orderpage.get_all_time_orders_total()
        mainpage.go_to_site(Urls.URL)
        mainpage.create_new_order()
        mainpage.go_to_order_list()
        after_total = orderpage.get_all_time_orders_total()
        assert before_total < after_total

    @allure.title('Проверка увеличения счетчика заказов за сегодня - после создания заказа')
    def test_today_orders_counter(self, driver, user_sign_in):
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.go_to_order_list()
        before_total = orderpage.get_today_orders_total()
        mainpage.go_to_site(Urls.URL)
        mainpage.create_new_order()
        mainpage.go_to_order_list()
        after_total = orderpage.get_today_orders_total()
        assert before_total < after_total

    @allure.title('Проверка наличия созданного заказ в списке заказов в работе')
    def test_new_order_in_work(self, driver, user_sign_in):
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        new_order = mainpage.create_new_order()
        mainpage.go_to_order_list()
        orderpage.wait_until_element_invisibility(20, OrderListPageLocators.ALL_READY_TITLE)
        order_in_work = orderpage.get_order_number_in_work()
        assert new_order in order_in_work