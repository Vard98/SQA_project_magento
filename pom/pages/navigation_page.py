from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class NavigationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    WOMEN_BUTTON = (By.ID, 'ui-id-4')
    TOPS_BUTTON = (By.ID, 'ui-id-9')
    HOODIES_AND_SWEATSHIRTS_BUTTON = (By.ID, 'ui-id-12')
    MEN_BUTTON = (By.ID, 'ui-id-5')
    BOTTOMS_BUTTON = (By.ID, 'ui-id-18')
    SHORTS_BUTTON = (By.ID, 'ui-id-24')

    def open_women_tops_hoodies(self):
        self.hover(self.get_wait().wait_for_element(self.WOMEN_BUTTON))
        self.hover(self.get_wait().wait_for_element(self.TOPS_BUTTON))
        self.click(self.get_wait().wait_for_element(self.HOODIES_AND_SWEATSHIRTS_BUTTON))

    def open_men_bottoms_shorts(self):
        self.hover(self.get_wait().wait_for_element(self.MEN_BUTTON))
        self.hover(self.get_wait().wait_for_element(self.BOTTOMS_BUTTON))
        self.click(self.get_wait().wait_for_element(self.SHORTS_BUTTON))
