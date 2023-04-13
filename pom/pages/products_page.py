from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PRODUCT_ITEM = (By.CSS_SELECTOR, "[class='product-item-info']")
    PRODUCT_SIZE = (By.CSS_SELECTOR, "[id='option-label-size-143-item-167']")
    PRODUCT_SIZE_MAN = (By.CSS_SELECTOR, "[id='option-label-size-143-item-175']")
    PRODUCT_COLOR = (By.CSS_SELECTOR, "[id='option-label-color-93-item-53']")
    PRODUCT_COLOR_MAN = (By.CSS_SELECTOR, "[id='option-label-color-93-item-49']")
    PRODUCT_QTY = (By.CSS_SELECTOR, "[id='qty']")
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "[id='product-addtocart-button']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='message-success success message']")
    SIZE_ERROR_MESSAGE = (By.CSS_SELECTOR, "div[id='super_attribute[143]-error']")
    COLOR_ERROR_MESSAGE = (By.CSS_SELECTOR, "div[id='super_attribute[93]-error']")
    SHOPPING_CART_BUTTON = (By.LINK_TEXT, "shopping cart")

    def select_product(self, index: int):
        products_list = self.find_list_of_elements(self.PRODUCT_ITEM)
        self.click(products_list[index])

    def select_product_size(self):
        product_size = self.get_wait().wait_for_element(self.PRODUCT_SIZE)
        self.click(product_size)

    def select_man_product_size(self):
        product_size = self.get_wait().wait_for_element(self.PRODUCT_SIZE_MAN)
        self.click(product_size)

    def select_product_color(self):
        product_color = self.get_wait().wait_for_element(self.PRODUCT_COLOR)
        self.click(product_color)

    def select_man_product_color(self):
        product_color = self.get_wait().wait_for_element(self.PRODUCT_COLOR_MAN)
        self.click(product_color)

    def select_product_qty(self, qty: str):
        product_qty = self.get_wait().wait_for_element(self.PRODUCT_QTY)
        self.click(product_qty)
        self.clear_field(product_qty)
        self.send_key(product_qty, qty)

    def click_add_to_card_button(self):
        add_to_card_button = self.get_wait().wait_for_element(self.ADD_TO_CARD_BUTTON)
        self.click(add_to_card_button)

    def get_success_message(self):
        message_field = self.get_wait().wait_for_element(self.SUCCESS_MESSAGE)
        return message_field.text

    def get_size_error_message(self):
        message_field = self.get_wait().wait_for_element(self.SIZE_ERROR_MESSAGE)
        return message_field.text

    def get_color_error_message(self):
        message_field = self.get_wait().wait_for_element(self.COLOR_ERROR_MESSAGE)
        return message_field.text

    def open_shopping_cart(self):
        shopping_cart_button = self.get_wait().wait_for_element_to_be_clickable(self.SHOPPING_CART_BUTTON)
        self.click(shopping_cart_button)
