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
    CHECKBOX_BUTTON = (By.ID, "sorter")
    SORT_BY_PRICE_BUTTON = (By.CSS_SELECTOR, "option[value = 'price']")
    SORT_BY_PRODUCT_NAME_BUTTON = (By.CSS_SELECTOR,"option[value = 'name']")
    COMPARE_BUTTON = (By.XPATH, '//*[text() = "Add to Compare"]')
    ADD_ALL_TO_CART_BUTTON = (By.XPATH, '//*[text()="Add All to Cart"]')
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, '//*[text() = "Add to Wish List"]')
    WISHLIST_LINK = (By.XPATH, '//*[text() ="Go to Wish List"]')

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
        
        def click_checkbox(self):
        self.get_wait().wait_for_element(self.CHECKBOX_BUTTON).click()

    def click_sort_by_price(self):
        self.get_wait().wait_for_element_to_be_clickable(self.SORT_BY_PRICE_BUTTON).click()

    def click_sort_by_product_name(self):
        self.get_wait().wait_for_element_to_be_clickable(self.SORT_BY_PRODUCT_NAME_BUTTON).click()

    def click_add_to_compare(self):
        self.get_wait().wait_for_element_to_be_clickable(self.COMPARE_BUTTON).click()

    def get_compare_success_message(self):
        compare_message = self.get_wait().wait_for_element(self.SUCCESS_MESSAGE)
        return compare_message.text

    def go_to_wishlist(self):
        self.get_wait().wait_for_element(self.WISHLIST_LINK).click()

    def click_add_all_to_cart(self):
        self.get_wait().wait_for_element_to_be_clickable(self.ADD_ALL_TO_CART_BUTTON).click()

    def click_add_to_wishlist(self):
        self.get_wait().wait_for_element_to_be_clickable(self.ADD_TO_WISHLIST_BUTTON).click()

    def get_add_to_wishlist_success_message(self):
        wishlist_message = self.get_wait().wait_for_element(self.SUCCESS_MESSAGE)
        return wishlist_message.text
