import allure
from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step('Нажимаем на Восстановить пароль')
    def click_link_password_reset(self):
        self.click_element(AuthPageLocators.LINK_PASSWORD_RESET)