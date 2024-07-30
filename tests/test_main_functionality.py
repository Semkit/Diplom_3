import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.locators import MainPageLocators
from utils.api import URL

class TestMainFunctionality:

    @allure.title('переход по клику на «Конструктор»')
    def test_go_to_order_feed(self, web_driver):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.ORDERS_LIST_URL)
        main_page.wait_for_overlay_to_be_invisible()
        main_page.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)
        main_page.constructor_button_click()
        main_page.wait_for_element(MainPageLocators.BURGER_CONSTRUCTOR)

        assert main_page.get_current_url() == URL.MAIN_PAGE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_constructor(self, web_driver):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.MAIN_PAGE_URL)
        main_page.wait_for_overlay_to_be_invisible()
        main_page.orders_button_click()
        main_page.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)

        assert main_page.get_current_url() == URL.ORDERS_LIST_URL

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями,')
    def test_select_ingredient(self, web_driver):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.MAIN_PAGE_URL)
        main_page.wait_for_element(MainPageLocators.INGREDIENT_ITEM)
        main_page.ingredient_click()
        result = main_page.wait_for_element(MainPageLocators.DETAILS_OF_INGREDIENT)

        assert result.is_displayed

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_popup(self, web_driver):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.MAIN_PAGE_URL)
        main_page.wait_for_element(MainPageLocators.INGREDIENT_ITEM)
        main_page.ingredient_click()
        main_page.wait_for_element(MainPageLocators.DETAILS_OF_INGREDIENT)
        main_page.ingredient_popup_close_button_click()

        assert main_page.wait_while_be_clickable(MainPageLocators.INGREDIENT_ITEM) == True

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_drag_and_drop_increase_counter(self, web_driver):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.MAIN_PAGE_URL)
        main_page.ingredient_drag_and_drop_to_basket()

        assert main_page.ingredient_return_counter() == '2', 'В Firefox не работает метод Drag and Drop'

    @allure.title('залогиненный пользователь может оформить заказ')

    def test_authorized_user_create_order(self, web_driver, create_user_and_delete_user):
        main_page = MainPage(web_driver)
        main_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page = LoginPage(web_driver)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        result = main_page.wait_for_element(MainPageLocators.ORDER_PREPARATION)

        assert result.is_displayed
