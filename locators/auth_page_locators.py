from selenium.webdriver.common.by import By


class AuthPageLocators:
    BUTTON_ENTER = (By.XPATH, '//button[text()="Войти"]')  #кнопка Войти на странице авторизации
    LINK_PASSWORD_RESET = (By.XPATH, '//*[@href="/forgot-password"]')  #ссылка Восстановить пароль на странице авторизации
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода емейла
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')  # поле ввода пароля