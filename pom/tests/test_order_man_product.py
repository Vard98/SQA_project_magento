import pytest
from pom.pages.navigation_page import NavigationPage
from pom.pages.products_page import ProductsPage
from pom.pages.shopping_page import ShoppingPage


@pytest.mark.usefixtures("set_up")
@pytest.mark.usefixtures("log_in")
class TestOrderManProduct:

    def test_product_selecting(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_men_bottoms_shorts()
        products_page.select_product(0)
        products_page.select_man_product_size()
        products_page.select_man_product_color()
        products_page.select_product_qty('2')
        products_page.click_add_to_card_button()
        message = products_page.get_success_message()
        assert message == "You added Pierce Gym Short to your shopping cart."

    def test_required_actions(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_men_bottoms_shorts()
        products_page.select_product(0)
        products_page.click_add_to_card_button()
        size_error_message = products_page.get_size_error_message()
        color_error_message = products_page.get_color_error_message()
        error_message = "This is a required field."
        assert size_error_message == error_message
        assert color_error_message == error_message

    def test_shipping_method(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        shopping_page = ShoppingPage(self.driver)
        navigation_page.open_men_bottoms_shorts()
        products_page.select_product(1)
        products_page.select_man_product_size()
        products_page.select_man_product_color()
        products_page.select_product_qty('3')
        products_page.click_add_to_card_button()
        products_page.open_shopping_cart()
        shopping_page.click_checkout_button()
        shopping_page.click_next_button()
        message = shopping_page.get_shipping_method_error()
        assert message == "The shipping method is missing. Select the shipping method and try again."

    def test_product_purchase(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        shopping_page = ShoppingPage(self.driver)
        navigation_page.open_men_bottoms_shorts()
        products_page.select_product(1)
        products_page.select_man_product_size()
        products_page.select_man_product_color()
        products_page.select_product_qty('3')
        products_page.click_add_to_card_button()
        products_page.open_shopping_cart()
        shopping_page.click_checkout_button()
        shopping_page.choose_shipping_method()
        shopping_page.click_next_button()
        shopping_page.place_order()
        message = shopping_page.get_thank_you_message()
        assert message == "Thank you for your purchase!"
