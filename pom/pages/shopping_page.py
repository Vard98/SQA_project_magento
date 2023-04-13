from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class ShoppingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-role='proceed-to-checkout']")
    SHIPPING_METHOD_RADIOBUTTON = (By.CSS_SELECTOR, "input[name='ko_unique_1']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button[data-role='opc-continue']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button[title='Place Order']")
    THANK_YOU_MESSAGE = (By.CSS_SELECTOR, "span[data-ui-id='page-title-wrapper']")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "a[class='action primary continue']")
    SHIPPING_METHOD_ERROR = (By.CSS_SELECTOR, "div[class='message notice']")

    def click_checkout_button(self):
        checkout_button = self.get_wait().wait_for_element_to_be_clickable(self.CHECKOUT_BUTTON)
        self.click(checkout_button)

    def choose_shipping_method(self):
        shipping_method_radiobutton = self.get_wait().wait_for_element(self.SHIPPING_METHOD_RADIOBUTTON)
        self.click(shipping_method_radiobutton)

    def click_next_button(self):
        next_button = self.get_wait().wait_for_element(self.NEXT_BUTTON)
        self.scroll(next_button)
        self.click(next_button)

    def place_order(self):
        place_order_button = self.get_wait().wait_for_element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        self.click(place_order_button)
        self.click(place_order_button)

    def get_thank_you_message(self):
        self.get_wait().wait_for_element(self.CONTINUE_SHOPPING_BUTTON)
        message_field = self.get_wait().wait_for_element(self.THANK_YOU_MESSAGE)
        return message_field.text

    def get_shipping_method_error(self):
        message_field = self.get_wait().wait_for_element(self.SHIPPING_METHOD_ERROR)
        return message_field.text
