import pytest

from pom.pages.customer_login import LoginPage


@pytest.mark.usefixtures("set_up")
class TestCustomerLogin:

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        login_page.click_on_sign_in_link()
        exp_msg = "Welcome, Test User!"
        login_page.login("testuser@gmail.com", 'TestUser1234()')
        logged_in_user_element = login_page.verify_login_with_correct_user()
        logged_in_user = logged_in_user_element.text
        assert exp_msg == logged_in_user

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        login_page.click_on_sign_in_link()
        alert_text = "Incorrect CAPTCHA"
        login_page.login("testuser@gmail.co", 'TestPass1234()')
        invalid_login_alert_element = login_page.verify_invalid_login_alert()
        invalid_login_alert = invalid_login_alert_element.text
        assert alert_text == invalid_login_alert

    def test_login_without_email_field(self):
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        login_page.click_on_sign_in_link()
        exp_alert_msg = 'This is a required field.'
        login_page.login("", 'TestPass1234()')
        email_alert_msg_element = login_page.verify_email_required_message()
        email_alert_msg = email_alert_msg_element.text
        assert exp_alert_msg == email_alert_msg

    def test_login_without_password_field(self):
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_load()
        login_page.click_on_sign_in_link()
        exp_alert_msg = 'This is a required field.'
        login_page.login("testuser@gmail.com", "")
        password_alert_msg_element = login_page.verify_password_required_message()
        password_alert_msg = password_alert_msg_element.text
        assert exp_alert_msg == password_alert_msg
