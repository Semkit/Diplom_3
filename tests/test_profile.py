import allure
from utils.api import URL
from utils.locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_profile(self, web_driver):
        profile_page = ProfilePage(web_driver)
        profile_page.set_current_url(URL.MAIN_PAGE_URL)
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.profile_button_click()

        assert profile_page.get_current_url() == URL.LOGIN_PAGE_URL


    @allure.title('переход в раздел «История заказов»')
    def test_go_to_order_history(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        profile_page = ProfilePage(web_driver)
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.profile_button_click()
        profile_page.wait_for_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.orders_history_button_click()

        assert profile_page.get_current_url() == URL.ORDER_HISTORY_PAGE_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        profile_page = ProfilePage(web_driver)
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.profile_button_click()
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.logout_button_click()
        profile_page.wait_for_overlay_to_be_invisible()
        profile_page.wait_for_element(ProfilePageLocators.ENTER_HEADER)

        assert profile_page.get_current_url() == URL.LOGIN_PAGE_URL
