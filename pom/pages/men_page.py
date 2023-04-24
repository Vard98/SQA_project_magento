from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage

class MenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    JACKETS_BUTTON = (By.XPATH, '//a[text()="Jackets"]')
    NAVIGATE_JACKETS_PAGE = (By.CSS_SELECTOR, 'span[class="base"]')

    def navigate_jackets_page(self):
        self.get_wait().wait_for_element(self.JACKETS_BUTTON).click()
        # self.get_wait().wait_for_element(self.NAVIGATE_JACKETS_PAGE).click()




