from pages.base_page import BasePage
from utils.locators import ProfilePageLocators
import allure

class ProfilePage(BasePage):


    def __init__(self, driver):
        self.driver = driver
    @allure.step('Нажимаем на кнопку Личный кабинет вверху страницы')
    def profile_button_click(self):
        self.click_element(ProfilePageLocators.PROFILE_BUTTON)

    @allure.step('Нажимаем на кнопку История заказов в личном кабинете')
    def orders_history_button_click(self):
        self.click_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Нажимаем на Выход в личном кабинете')
    def logout_button_click(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Нажимаем на заказ из Истории заказов')
    def order_history_field_click(self):
        self.click_element(ProfilePageLocators.ORDERS_HISTORY_FIELD)