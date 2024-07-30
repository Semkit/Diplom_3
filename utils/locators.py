from selenium.webdriver.common.by import By

class BasePageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")# Кнопка-эмблема "Конструктор" в шапке
    ORDERS_LOGO = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка-эмблема "Лента Заказов" в шапке
    MAIN_LAYOUT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']") # Оверлей для бразуера Firefox

class LoginPageLocators(BasePageLocators):
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") # Кнопка "Восстановить пароль" на странице входа в аккаунт
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']") # Кнопка "Восстановить" на странице восстановление пароля
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  # поле "E-mail" для ввода
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  # поле "Пароль" для ввода
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти" на странице входа пользователя
    ENTER_BUTTON_MAIN_PAGE = (
    By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    ENTER_CODE = (
    By.XPATH, "//label[text()='Введите код из письма']")  # Поле для ввода кода из письма при восстановлении пароля
    TOGGLE_PASSWORD_VISIBILITY = (
    By.XPATH, "//*[@class = 'input__icon input__icon-action']")  # Кнопка-картинка "глаз" чтобы показать пароль
    VISIBLE_PASS = (By.XPATH,
                    "//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # Активное поле с видимым паролем

class MainPageLocators(BasePageLocators):
    BURGER_CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # Форма собирания бургера
    ORDER_FEED_BUTTON = (By.XPATH, " //h1[text()='Лента заказов']") # Кнопка "Лента заказов"
    INGREDIENT_POPUP_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')][1]") # Кнопка закрытия окна "Детали ингредиента"
    BUTT_MAIN_PAGE = (By.XPATH,
                      ".//button[contains(@class, 'button_button_type_primary')]")  # Кнопка "Войти в аккаунт" и "Оформить заказ" на главной странице сервиса
    INGREDIENT_ITEM = (By.XPATH, ".//img[@alt='Краторная булка N-200i']")  # локатор примера ингредиента
    DETAILS_OF_INGREDIENT = (By.XPATH,
                             "//*[@class = 'Modal_modal__container__Wo2l_']")  # Всплывающее окно "Детали ингредиента" при нажатии на ингредиент
    ORDER_BASKET = (By.XPATH, "//*[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']")  # локатор корзины заказа
    INGREDIENT_ITEM_COUNTER = (By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__list')][1]/a[2]/div[1]/p")  # локатор счетчика ингредиента в заказе
    ORDER_PREPARATION = (
    By.XPATH, "//*[contains(text(), 'Ваш заказ начали готовить')]")  # информация о начале готовки заказа

class ProfilePageLocators(BasePageLocators):
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") #кнопка "Личный кабинет" на главной странице
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']") #кнопка история заказов в личном кабинете
    ORDERS_HISTORY_FIELD = (By.XPATH, "//*[@class='OrderHistory_listItem__2x95r mb-6']")  # Поле с историей заказов на странице История заказов в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка "Войти" на странице входа пользователя
    ENTER_HEADER = (By.XPATH, "//h2[text()='Вход']") # Заголовок Вход на странице авторизации

class OrderFeedPageLocators(BasePageLocators):
    ORDER_DETAILS_BUTTON = (By.XPATH, "//button[contains(text(),'Детали заказа')]")
    FORM_ORDER_FEED = [By.XPATH, ".//div[contains(@class, 'OrderFeed_orderFeed__')]"]  # локатор страницы ленты заказов
    CLOSE_ORDER_INFO = (By.XPATH,
                        "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # Крестик закрыть окно с деталями заказа после оформления заявки
    ORDER_DETAILS = (By.XPATH,
                     "//p[@class='text text_type_main-medium mb-8']")  # Окно с деталями заказа, которое открывается в Истории заказов после нажатия на соответствующий заказ
    ORDER_NUMBER = (
    By.XPATH, "//p[text()='идентификатор заказа']")  # Окно с деталями заказа и его номером после оформления заказа
    TOTAL_ORDERS = (By.XPATH, "//*[contains(text(), 'за все время')]/following::p")  # счетчик заказов за все время
    TOTAL_ORDERS_TODAY = (By.XPATH, "//*[contains(text(), 'сегодня')]/following::p")  # счетчик заказов за сегодня
    ORDER_ID = (By.XPATH, "//*[contains(@class, 'Modal_modal__contentBox')]/child::h2")  # ID заказа после его создания
    ORDER_IN_WORK_BASE = (By.XPATH,
                          "//*[contains(@class, 'orderListReady')]/child::li[@class='text text_type_main-small']")  # номер заказа в статусе В работе
    ORDER_IN_WORK_NEW = (By.XPATH,
                         "//*[contains(@class, 'orderListReady')]/child::li[@class='text text_type_digits-default mb-2']")  # номер заказа в статусе В работе
