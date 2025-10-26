from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_LK = (By.XPATH, '//*[@href="/account"]')  # ссылка Личный кабинет в шапке лендинга
    CONSTRUCTOR_LINK = (By.XPATH, '//p[text()="Конструктор"]/parent::a')  # ссылка Конструктор в шапке лендинга
    ORDER_LIST_LINK = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # ссылка Лента Заказов в шапке лендинга
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')   # кнопка Войти в аккаунт
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')  # заголовок Соберите бургер
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка Оформить заказ
    BUN_IN_BASKET = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3 (верх)"]')  # булка в корзине
    INGREDIENT_BUN = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]') #ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]') #счетчик ингредиента Флюоресцентная булка R2-D3
    INGREDIENT_POPUP_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]') # заголовок всплывающего окна Детали ингредиента
    INGREDIENT_POPUP = (By.XPATH, '//*[contains(@class, "contentBox")]')  # всплывающее окно Детали ингредиента
    ORDER_BASKET = (By.XPATH, '//ul[contains(@class,"basket")]')  #Корзина
    ORDER_NUMBER = (By.XPATH, '//*[contains(@class, "type_digits-large")]') # номер заказа во всплывающем окне
    DEFAULT_ORDER = (By.XPATH, '//h2[text()="9999"]') #стандартный номер заказа в попапе
    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]') #Ваш заказ начали готовить в попапе
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]') #Крестик закрытия попапа