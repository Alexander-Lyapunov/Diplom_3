import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data.urls import Urls
from helpers import create_new_user
from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.step('Запуск driver')
@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
    elif request.param == 'Chrome':
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@allure.step('Создание пользователя с дальнейшим удалением')
@pytest.fixture
def create_user():
    email, password, token = create_new_user()
    yield email, password, token
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Authorization': f'{token}'})

@allure.step('Авторизация пользователя')
@pytest.fixture
def user_sign_in(driver, create_user):
    mainpage = MainPage(driver)
    mainpage.go_to_site(Urls.URL)
    mainpage.click_element(MainPageLocators.ENTER_BUTTON)
    mainpage.send_keys(AuthPageLocators.INPUT_EMAIL, create_user[0])
    mainpage.send_keys(AuthPageLocators.INPUT_PASSWORD, create_user[1])
    mainpage.wait_until_element_visibility(10, AuthPageLocators.BUTTON_ENTER)
    mainpage.click_element(AuthPageLocators.BUTTON_ENTER)
    mainpage.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)



