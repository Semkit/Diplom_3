from pages.base_page import BasePage
from utils.locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Логинимся под пользователем')
    def login_user(self, email, password):
        self.wait_for_overlay_to_be_invisible()
        self.click_element(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        self.data_input_into_locator(LoginPageLocators.EMAIL_FIELD, email)
        self.data_input_into_locator(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Прокидываем данные в локатор (если он поле ввода данных)')
    def data_input_into_locator(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)
