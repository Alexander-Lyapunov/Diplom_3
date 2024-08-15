from selenium.webdriver.common.by import By


class LKPageLocators:
    PROFILE_LINK = (By.XPATH, '//*[@href="/account/profile"]')  # cсылка Профиль в ЛК
    ORDER_HISTORY_LINK = (By.XPATH, '//*[@href="/account/order-history"]')  # cсылка История заказов в ЛК
    BUTTON_EXIT = (By.XPATH, '//*[contains(@class, "Account_button")]')  # кнопка Выход
    NUMBERS_ORDERS_LIST = (By.XPATH, "//p[@class='text text_type_digits-default']")  # Список заказове
