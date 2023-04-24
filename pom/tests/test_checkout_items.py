import pytest

from pom.pages.men_page import MenPage
from pom.pages.home_page import HomePage
from pom.pages.jackets_page import JacketsPage


@pytest.mark.usefixtures("set_up")
class TestCheckoutItems:

    def test_counts_of_item_in_cart(self):
        home_page = HomePage(self.driver)
        men_page = MenPage(self.driver)
        jackets_page = JacketsPage(self.driver)
        home_page.wait_for_page_load()
        home_page.navigate_men_page()
        men_page.wait_for_page_load()
        men_page.navigate_jackets_page()
        jackets_page.wait_for_page_load()
        jackets_page.choose_jacket()
        jackets_page.open_cart()
        assert jackets_page.get_items_count().text == "1 Item in Cart", "The item is not added to the cart"

    def test_add_multiple_items_in_cart(self):
        home_page = HomePage(self.driver)
        men_page = MenPage(self.driver)
        jackets_page = JacketsPage(self.driver)
        home_page.wait_for_page_load()
        home_page.navigate_men_page()
        men_page.wait_for_page_load()
        men_page.navigate_jackets_page()
        jackets_page.wait_for_page_load()
        jackets_page.choose_jacket()
        jackets_page.wait_for_page_load()
        jackets_page.open_cart()
        jackets_page.scroll_to_wind_jacket()
        jackets_page.add_wind_jacket_to_checkout_cart()
        jackets_page.scroll_to_checkout_cart()
        assert jackets_page.checkout_items_count().text == "2 Items in Cart", "The item is not added to the cart"

    def test_remove_item_from_cart(self):
        home_page = HomePage(self.driver)
        men_page = MenPage(self.driver)
        jackets_page = JacketsPage(self.driver)
        home_page.wait_for_page_load()
        home_page.navigate_men_page()
        men_page.wait_for_page_load()
        men_page.navigate_jackets_page()
        jackets_page.wait_for_page_load()
        jackets_page.choose_jacket()
        jackets_page.wait_for_page_load()
        jackets_page.open_cart()
        jackets_page.scroll_to_wind_jacket()
        jackets_page.add_wind_jacket_to_checkout_cart()
        jackets_page.scroll_to_checkout_cart()
        jackets_page.remove_item_from_cart()
        jackets_page.click_alert_button()
        check_deleted_items_quantity = jackets_page.check_the_items_quantity()
        assert check_deleted_items_quantity.text == "1 Item in Cart", "The item is not added to the cart"
