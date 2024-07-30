from selenium.webdriver.support import expected_conditions
from utils.api import URL
from utils.locators import BasePageLocators
from utils.locators import OrderFeedPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait

class OrderFeedPage(BasePage):


    @allure.step('Нажимаем на кнопку Закрыть окно информации о заказе после оформления заказа')
    def order_details_close_button_click(self):
        self.click_element(OrderFeedPageLocators.CLOSE_ORDER_INFO)

    @allure.step('Получаем значение счетчика заказов')
    def get_total_orders_counter(self, locator):
       self.set_current_url(URL.MAIN_PAGE_URL)
       self.wait_for_overlay_to_be_invisible()
       self.wait_for_element(BasePageLocators.ORDERS_LOGO)
       self.orders_button_click()
       self.wait_for_overlay_to_be_invisible()
       result = self.wait_for_element(locator).text

       return result

    @allure.step('Ожидаем пока поменяется текст в локаторе')
    def wait_while_text_change(self):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(OrderFeedPageLocators.ORDER_ID,'9999'))