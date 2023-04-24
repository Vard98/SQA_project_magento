from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MEN_BUTTON = (By.XPATH, '//span[text()="Men"]')
    NAVIGATE_MEN_PAGE = (By.CSS_SELECTOR, 'span[class="base"]')

    def navigate_men_page(self):
        self.get_wait().wait_for_element(self.MEN_BUTTON).click()

        # self.get_wait().wait_for_element(self.NAVIGATE_MEN_PAGE)








