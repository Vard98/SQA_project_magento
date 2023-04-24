from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
import time


class JacketsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    CHOOSE_JACKET_SIZE = (By.XPATH, '(//div[@id="option-label-size-143-item-168"])[1]')
    CHOOSE_COLOR = (By.XPATH, '(//div[@id="option-label-color-93-item-50"])[1]')
    ADD_CART = (By.XPATH, '//span[text()="Add to Cart"]')
    CHECKOUT_CART = (By.CSS_SELECTOR, 'a[class="action showcart"]')
    ITEMS_COUNT = (By.CSS_SELECTOR, 'div[class="items-total"]')
    WIND_JACKET_SIZE = (By.XPATH, '(//div[@id="option-label-size-143-item-168"])[2]')
    WIND_JACKET_COLOR = (By.XPATH, '(//div[@id="option-label-color-93-item-53"])[1]')
    WIND_JACKET_ADD_CART = (By.XPATH, '(//span[text()="Add to Cart"])[2]')
    CHECK_ITEMS_COUNT = (By.CSS_SELECTOR, 'div[class="items-total"]')
    REMOVE_ITEM_BUTTON = (By.XPATH, '(//a[@class="action delete"])[1]')
    ALERT_BUTTON = (By.CSS_SELECTOR, '[class="action-primary action-accept"]')
    THE_ITEMS_COUNT = (By.CSS_SELECTOR, '[class="items-total"]')
    LOGO_LUMA = (By.XPATH, '//a[@class="logo"]')

    def choose_jacket(self):
        jacket_size = self.get_wait().wait_for_element(self.CHOOSE_JACKET_SIZE)
        self.click(jacket_size)
        jacket_color = self.get_wait().wait_for_element(self.CHOOSE_COLOR)
        self.click(jacket_color)
        add_cart = self.get_wait().wait_for_element(self.ADD_CART)
        self.click(add_cart)

    def open_cart(self):
        open_cart_fild = self.get_wait().wait_for_element(self.CHECKOUT_CART)
        self.scroll(open_cart_fild)
        time.sleep(3)
        self.click(open_cart_fild)

    def get_items_count(self):
        items_count = self.get_wait().wait_for_element(self.ITEMS_COUNT)
        return items_count

    def scroll_to_wind_jacket(self):
        scroll_down = self.get_wait().wait_for_element(self.WIND_JACKET_SIZE)
        self.scroll(scroll_down)

    def add_wind_jacket_to_checkout_cart(self):
        wind_jacket_size = self.get_wait().wait_for_element(self.WIND_JACKET_SIZE)
        self.click(wind_jacket_size)
        color_of_wind_jacket = self.get_wait().wait_for_element(self.WIND_JACKET_COLOR)
        self.click(color_of_wind_jacket)
        click_add_cart = self.get_wait().wait_for_element(self.WIND_JACKET_ADD_CART)
        self.click(click_add_cart)

    def scroll_to_checkout_cart(self):
        scroll_to_items_count = self.get_wait().wait_for_element(self.CHECKOUT_CART)
        self.scroll(scroll_to_items_count)
        time.sleep(3)
        self.click(scroll_to_items_count)

    def checkout_items_count(self):
        check_items_count = self.get_wait().wait_for_element(self.CHECK_ITEMS_COUNT)
        check_items_count.click()
        return check_items_count

    def remove_item_from_cart(self):
        click_remove_item = self.get_wait().wait_for_element(self.REMOVE_ITEM_BUTTON)
        self.click(click_remove_item)

    def click_alert_button(self):
        click_alert = self.get_wait().wait_for_element(self.ALERT_BUTTON)
        time.sleep(2)
        self.click(click_alert)

    def check_the_items_quantity(self):
        check_quantity = self.get_wait().wait_for_button(self.THE_ITEMS_COUNT)
        time.sleep(3)
        self.click(check_quantity)
        return check_quantity
