from selenium.webdriver.common.by import By


class PasswordResetPageLocators:
    RESET_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка Восстановить
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')  # кнопка Сохранить
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]') #кнопка Показать/скрыть пароль
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода емейла
    INPUT_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')  #поле Пароль активно