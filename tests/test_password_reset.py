import allure
from data.urls import Urls
from locators.password_reset_locators import PasswordResetPageLocators
from pages.auth_page import AuthPage
from pages.password_reset_page import PasswordResetPage
from conftest import *


class TestPasswordReset:
    @allure.title('Нажатие на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        authpage = AuthPage(driver)
        authpage.go_to_site(Urls.URL_LOGIN)
        authpage.click_link_password_reset()
        assert authpage.get_current_url() == Urls.URL_FORGOT_PASSWORD

    @allure.title('Ввод емейла и нажатие кнопки Восстановить')
    def test_input_email_and_click_reset(self, driver, create_user):
        passpage = PasswordResetPage(driver)
        passpage.go_to_site(Urls.URL_FORGOT_PASSWORD)
        passpage.input_email_for_reset_password(create_user[0])
        passpage.click_reset_password_button()
        assert passpage.get_current_url() == Urls.URL_RESET_PASSWORD

    @allure.title('Подсветка поля Пароль после нажатия на кнопку Показать/скрыть пароль')
    def test_password_input_active(self, driver, create_user):
        passpage = PasswordResetPage(driver)
        passpage.go_to_site(Urls.URL_FORGOT_PASSWORD)
        passpage.input_email_for_reset_password(create_user[0])
        passpage.click_reset_password_button()
        passpage.click_show_password()
        assert passpage.find_element(PasswordResetPageLocators.INPUT_ACTIVE).is_displayed()