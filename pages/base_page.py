import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        url = self.driver.current_url
        return url

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание появления элемента')
    def wait_until_element_visibility(self, time, locator):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Создание элементов для получения списка')
    def element_list(self, locator: tuple):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception(f'{elements} не найден')
        return elements

    @allure.step('Ожидание исчезновения элемента')
    def wait_until_element_invisibility(self, time, locator):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидание URL')
    def wait_until_url_to_be(self, time, expected_url):
        WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Ввод текста')
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Перетаскивание элемента')
    def drag_and_drop(self, drag, drop):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(drag))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(drop))
        drag = self.driver.find_element(*drag)
        drop = self.driver.find_element(*drop)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()