import allure
from utils.locators import ProfilePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from utils.api import URL
from pages.profile_page import ProfilePage
from utils.locators import OrderFeedPageLocators

class TestOrderFeedPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        order_feed_page = OrderFeedPage(web_driver)
        profile_page = ProfilePage(web_driver)
        main_page = MainPage(web_driver)

        order_feed_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_NUMBER)
        order_feed_page.wait_for_overlay_to_be_invisible()
        order_feed_page.order_details_close_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        profile_page.profile_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        profile_page.wait_for_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        profile_page.orders_history_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        profile_page.wait_for_element(ProfilePageLocators.ORDERS_HISTORY_FIELD)
        profile_page.order_history_field_click()
        result = order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_DETAILS)

        assert result.is_displayed    #В Firefox не работает drag and drop, так что заказ автоматически не создаётся
                                        # и для него тест падает

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_are_visible_in_profile(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        order_feed_page = OrderFeedPage(web_driver)
        profile_page = ProfilePage(web_driver)
        main_page = MainPage(web_driver)

        order_feed_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_NUMBER)
        order_feed_page.wait_for_overlay_to_be_invisible()
        order_feed_page.order_details_close_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        profile_page.profile_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        profile_page.orders_history_button_click()
        result = profile_page.wait_for_element(ProfilePageLocators.ORDERS_HISTORY_FIELD)

        assert result.is_displayed #В Firefox не работает drag and drop, так что заказ автоматически не создаётся
                                        # и для него тест падает

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_check_total_orders_counter(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        order_feed_page = OrderFeedPage(web_driver)
        main_page = MainPage(web_driver)

        total_counter_before = order_feed_page.get_total_orders_counter(OrderFeedPageLocators.TOTAL_ORDERS)
        print(f"{total_counter_before} было заказов на текущий момент всего")
        order_feed_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_NUMBER)
        order_feed_page.wait_for_overlay_to_be_invisible()
        order_feed_page.order_details_close_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        total_counter_after = order_feed_page.get_total_orders_counter(OrderFeedPageLocators.TOTAL_ORDERS)
        print(f"{total_counter_after} стало заказов после этого всего")

        assert total_counter_before < total_counter_after #В Firefox не работает drag and drop,
                                                    # так что заказ автоматически не создаётся
                                                    # и для него тест падает

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_check_total_orders_today_counter(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        order_feed_page = OrderFeedPage(web_driver)
        main_page = MainPage(web_driver)
        total_counter_before = order_feed_page.get_total_orders_counter(OrderFeedPageLocators.TOTAL_ORDERS_TODAY)
        print(f"{total_counter_before} было заказов на текущий момент сегодня")
        order_feed_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_NUMBER)
        order_feed_page.wait_for_overlay_to_be_invisible()
        order_feed_page.order_details_close_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        total_counter_after = order_feed_page.get_total_orders_counter(OrderFeedPageLocators.TOTAL_ORDERS_TODAY)
        print(f"{total_counter_after} стало заказов после этого сегодня")

        assert total_counter_before < total_counter_after #В Firefox не работает drag and drop,
                                                    # так что заказ автоматически не создаётся
                                                    # и для него тест падает


    @allure.title('после оформления заказа его номер появляется в разделе "В работе".')
    def test_check_order_number(self, web_driver, create_user_and_delete_user):
        login_page = LoginPage(web_driver)
        order_feed_page = OrderFeedPage(web_driver)
        main_page = MainPage(web_driver)
        order_feed_page.set_current_url(URL.MAIN_PAGE_URL)
        login_page.login_user(create_user_and_delete_user[1], create_user_and_delete_user[2])
        main_page.ingredient_drag_and_drop_to_basket()
        main_page.create_order_button_click()
        order_feed_page.wait_while_be_clickable(OrderFeedPageLocators.CLOSE_ORDER_INFO)
        order_feed_page.wait_while_text_change()
        order_id = order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_ID).text
        order_feed_page.order_details_close_button_click()
        order_feed_page.orders_button_click()
        order_feed_page.wait_for_overlay_to_be_invisible()
        order_in_work = order_feed_page.wait_for_element(OrderFeedPageLocators.ORDER_IN_WORK_NEW).text

        assert f'0{order_id}' == order_in_work #В Firefox не работает drag and drop,
                                                    # так что заказ автоматически не создаётся
                                                    # и для него тест падает