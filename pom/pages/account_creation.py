import time

from selenium.webdriver.common.by import By

from pom.base.base_page import BasePage


class AccountCreation(BasePage):
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[contains(text(),'Create an Account')]")
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    NEWSLETTER_CHECKBOX = (By.ID, 'is_subscribed')
    EMAIL_ADDRESS = (By.ID, 'email_address')
    PASSWORD_FIELD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'password-confirmation')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
    USED_EMAIL_ALERT_MESSAGE = (
    By.XPATH, "//div[contains(text(),'There is already an account with this email address. ')]")
    CREATED_USER_USERNAME = (By.CSS_SELECTOR, 'span.logged-in')

    def click_on_create_account_link(self):
        self.get_wait().wait_for_element(self.CREATE_ACCOUNT_LINK).click()

    def fill_first_name_field(self, firstname):
        element = self.get_wait().wait_for_element(self.FIRST_NAME)
        element.send_keys(firstname)

    def fill_last_name_field(self, lastname):
        element = self.get_wait().wait_for_element(self.LAST_NAME)
        element.send_keys(lastname)

    def select_checkbox(self):
        self.get_wait().wait_for_element(self.NEWSLETTER_CHECKBOX).click()

    def fill_email_field(self, email):
        element = self.get_wait().wait_for_element(self.EMAIL_ADDRESS)
        element.send_keys(email)

    def fill_password_field(self, password):
        element = self.get_wait().wait_for_element(self.PASSWORD_FIELD)
        element.send_keys(password)

    def fill_confirm_password_field(self, confirm_password):
        element = self.get_wait().wait_for_element(self.CONFIRM_PASSWORD)
        element.send_keys(confirm_password)

    def click_on_create_account_button(self):
        self.get_wait().wait_for_element(self.CREATE_ACCOUNT_BUTTON).click()

    def create_account(self, firstname, lastname, email, password, confirm_password):
        self.fill_first_name_field(firstname)
        self.fill_last_name_field(lastname)
        self.select_checkbox()
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.fill_confirm_password_field(confirm_password)
        self.click_on_create_account_button()
        time.sleep(5)

    def verify_created_user_account(self):
        return self.get_wait().wait_for_element(self.CREATED_USER_USERNAME)

    def verify_used_email_message(self):
        return self.get_wait().wait_for_element(self.USED_EMAIL_ALERT_MESSAGE)
