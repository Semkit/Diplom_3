import allure
from utils.api import URL
from utils.locators import LoginPageLocators
from pages.login_page import LoginPage

class TestLoginPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_password(self, web_driver):
        login_page = LoginPage(web_driver)
        login_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.wait_for_overlay_to_be_invisible()
        login_page.click_element(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

        assert login_page.get_current_url() == URL.FORGOT_PASSWORD_PAGE_URL

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_click_recovery(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        login_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.wait_for_overlay_to_be_invisible()
        login_page.click_element(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
        login_page.data_input_into_locator(LoginPageLocators.EMAIL_FIELD, create_user_and_delete_user[1])
        login_page.click_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
        login_page.wait_for_element(LoginPageLocators.ENTER_CODE)

        assert login_page.get_current_url() == URL.RESET_PASSWORD_PAGE_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_toggle_password_visibility(self, web_driver,create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        login_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.wait_for_overlay_to_be_invisible()
        login_page.click_element(LoginPageLocators.ENTER_BUTTON_MAIN_PAGE)
        login_page.data_input_into_locator(LoginPageLocators.PASSWORD_FIELD, create_user_and_delete_user[2])
        login_page.click_element(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY)

        visible_pass = login_page.wait_for_element(LoginPageLocators.VISIBLE_PASS)

        assert visible_pass.is_displayed