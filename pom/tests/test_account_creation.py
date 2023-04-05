import random
import string
import pytest

from pom.pages.account_creation import AccountCreation


@pytest.mark.usefixtures("set_up")
class TestAccountCreation:

    def test_account_creation_positive(self):
        account_creation = AccountCreation(self.driver)
        account_creation.get_wait().wait_for_page()
        account_creation.click_on_create_account_link()
        email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email_address = email_prefix + "@gmail.com"
        username = "Welcome, Testing User!"
        account_creation.create_account("Testing", "User", email_address, "TestPassword()", "TestPassword()")
        created_user_username_element = account_creation.verify_created_user_account()
        created_user_username = created_user_username_element.text
        assert created_user_username == username, f"Expected username {username}, but got {created_user_username}"

    def test_account_creation_with_already_existing_email(self):
        account_creation = AccountCreation(self.driver)
        account_creation.get_wait().wait_for_page()
        account_creation.click_on_create_account_link()
        error_msg = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
        account_creation.create_account("Testing", "User", "test_email@gmail.com", "TestPassword()", "TestPassword()")
        existing_username_element = account_creation.verify_used_email_message()
        existing_username = existing_username_element.text
        assert error_msg == existing_username
