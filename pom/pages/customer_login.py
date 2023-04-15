import time
from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SIGN_IN_LINK = (By.XPATH, "//a[contains(text(),'Sign In')]")
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'pass')
    SING_IN_BUTTON = (By.ID, 'send2')
    INVALID_CREDENTIALS_ALERT = (By.CSS_SELECTOR, 'div[role="alert"]')
    EMAIL_FIELD_ERROR_MESSAGE = (By.ID, 'email-error')
    PASSWORD_FIELD_ERROR_MESSAGE = (By.ID, 'pass-error')
    LOGGED_IN_USER_NAME = (By.CSS_SELECTOR, 'span.logged-in')

    def click_on_sign_in_link(self):
        self.get_wait().wait_for_element(self.SIGN_IN_LINK).click()

    def fill_username_field(self, username):
        element = self.get_wait().wait_for_element(self.EMAIL_FIELD)
        element.send_keys(username)

    def fill_password_field(self, password):
        self.find_element_by(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element_by(self.SING_IN_BUTTON).click()

    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_login()
        time.sleep(3)

    def verify_login_with_correct_user(self):
        return self.get_wait().wait_for_element(self.LOGGED_IN_USER_NAME)

    def verify_invalid_login_alert(self):
        return self.get_wait().wait_for_element(self.INVALID_CREDENTIALS_ALERT)

    def verify_email_required_message(self):
        return self.get_wait().wait_for_element(self.EMAIL_FIELD_ERROR_MESSAGE)

    def verify_password_required_message(self):
        return self.get_wait().wait_for_element(self.PASSWORD_FIELD_ERROR_MESSAGE)
