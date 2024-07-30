from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import BasePageLocators
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание элемента по локатору')
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент по локатору')
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Ожидание исчезновения элемента со страницы по локатору')
    @allure.description('Функция необходима для ожидания исчезновения оверлея бразуера Firefox.')
    def wait_for_overlay_to_be_invisible(self):
        WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(BasePageLocators.MAIN_LAYOUT))

    @allure.step('Запрос URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажатие на кнопку "Конструктор"')
    def constructor_button_click(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие на кнопку "Лента Заказов"')
    def orders_button_click(self):
        self.click_element(BasePageLocators.ORDERS_LOGO)

    @allure.step('Ввод URL')
    def set_current_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем пока элемент станет доступен для нажатия')
    def wait_while_be_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        return True

