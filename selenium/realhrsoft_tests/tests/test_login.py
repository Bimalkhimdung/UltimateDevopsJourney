import pytest
from realhrsoft_tests.pageobjects.login_page import LoginPage
from realhrsoft_tests.config.config import BASE_URL

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for each test"""
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.driver.get(BASE_URL)

    def test_navigate_to_login_page(self):
        """Test that we can navigate to login page"""
        assert BASE_URL in self.driver.current_url
        assert "RealHRsoft | Complete HR Intelligence" in self.driver.title

    def test_perform_forgot_password(self):
        """Test forgot password functionality"""
        self.login_page.perform_forgot_password(self.login_page.user_data['normal']['userEmail'])
        success_message = self.login_page.get_recovery_success_message()
        assert "A LINK HAS BEEN ATTACHED TO YOUR EMAIL FOR PASSWORD RECOVERY" in success_message

    def test_cannot_login_with_invalid_email(self):
        """Test login with invalid email"""
        self.login_page.login(
            self.login_page.user_data['invalid']['userEmail'],
            self.login_page.user_data['invalid']['userPassword']
        )
        # TODO: Add snackbar assertion
        # assert "Either user does not exist or username password was incorrect" in self.login_page.get_snackbar_message()

    def test_cannot_login_with_blank_email(self):
        """Test login with blank email"""
        self.login_page.login(" ", self.login_page.user_data['normal']['userPassword'])
        error_message = self.login_page.get_error_message()
        assert "The Username field is required" in error_message

    def test_cannot_login_with_invalid_password(self):
        """Test login with invalid password"""
        self.login_page.login(
            self.login_page.user_data['normal']['userEmail'],
            self.login_page.user_data['invalid']['userPassword']
        )
        # TODO: Add snackbar assertion
        # assert "Either user does not exist or username password was incorrect" in self.login_page.get_snackbar_message()

    def test_cannot_login_with_blank_password(self):
        """Test login with blank password"""
        self.login_page.login(self.login_page.user_data['invalid']['userEmail'], " ")
        error_message = self.login_page.get_error_message()
        assert "The Password field is required" in error_message

    def test_can_login_with_valid_credentials(self):
        """Test login with valid credentials"""
        self.login_page.login(
            self.login_page.user_data['normal']['userEmail'],
            self.login_page.user_data['normal']['userPassword']
        )
        assert "Noticeboard | RealHRsoft | Complete HR Intelligence" in self.driver.title
        # TODO: Add snackbar assertion
        # assert "Successfully Logged In" in self.login_page.get_snackbar_message()

    def test_can_login_with_valid_credentials_and_remember_me(self):
        """Test login with valid credentials and remember me"""
        self.login_page.login(
            self.login_page.user_data['normal']['userEmail'],
            self.login_page.user_data['normal']['userPassword'],
            remember_me=True
        )
        assert "Noticeboard | RealHRsoft | Complete HR Intelligence" in self.driver.title
        # TODO: Add snackbar assertion
        # assert "Successfully Logged In" in self.login_page.get_snackbar_message() 