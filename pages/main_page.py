import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utils.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

        def __init__(self, driver):
            self.driver = driver

        @allure.step('Нажимаем на пример ингредиента')
        def ingredient_click(self):
            self.click_element(MainPageLocators.INGREDIENT_ITEM)

        @allure.step('Нажимаем на кнопку Крестик в окне Детали ингредиента')
        def ingredient_popup_close_button_click(self):
            self.click_element(MainPageLocators.INGREDIENT_POPUP_CLOSE_BUTTON)

        @allure.step('Перетягиваем элемент в корзину')
        def ingredient_drag_and_drop_to_basket(self):
            drag = WebDriverWait(self.driver, 20).until(
                expected_conditions.element_to_be_clickable(MainPageLocators.INGREDIENT_ITEM))
            drop = WebDriverWait(self.driver, 20).until(
                expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BASKET))
            ActionChains(self.driver).drag_and_drop(drag, drop).perform()

        @allure.step('Возвращаем значение счетчика ингредиента')
        def ingredient_return_counter(self):
            result = WebDriverWait(self.driver, 20).until(
                expected_conditions.visibility_of_element_located(MainPageLocators.INGREDIENT_ITEM_COUNTER)).text
            return result

        @allure.step('Нажимаем на кнопку Оформить заказ')
        def create_order_button_click(self):
            self.click_element(MainPageLocators.BUTT_MAIN_PAGE)
