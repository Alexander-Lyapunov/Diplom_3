import allure
from locators.password_reset_locators import PasswordResetPageLocators
from pages.base_page import BasePage


class PasswordResetPage(BasePage):
    @allure.step('Вводим емейл в поле для восстановления пароля')
    def input_email_for_reset_password(self, email):
        self.send_keys(PasswordResetPageLocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_password_button(self):
        self.wait_until_element_visibility(20, PasswordResetPageLocators.RESET_BUTTON)
        self.click_element(PasswordResetPageLocators.RESET_BUTTON)
        self.wait_until_element_visibility(20, PasswordResetPageLocators.SAVE_BUTTON)

    @allure.step('Кликаем на иконку Показать/скрыть пароль')
    def click_show_password(self):
        self.click_element(PasswordResetPageLocators.SHOW_PASSWORD_BUTTON)