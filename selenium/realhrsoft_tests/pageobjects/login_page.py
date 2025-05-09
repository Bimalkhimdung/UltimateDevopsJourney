from selenium.webdriver.common.by import By
from realhrsoft_tests.pageobjects.base_page import BasePage
import json
import os

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Forgot Password?')]")
    RECOVERY_EMAIL_INPUT = (By.ID, "email")
    SUBMIT_RECOVERY_BUTTON = (By.XPATH, "//button[@type='submit']")
    RECOVERY_SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")
    SNACKBAR_MESSAGE = (By.CLASS_NAME, "toast-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.load_test_data()

    def load_test_data(self):
        """Load test data from JSON files"""
        base_path = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(base_path, 'test_data', 'users.json'), 'r') as f:
            self.user_data = json.load(f)

    def login(self, username, password, remember_me=False):
        """Perform login with given credentials"""
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        if remember_me:
            self.click_element(*self.REMEMBER_ME_CHECKBOX)
        self.click_element(*self.LOGIN_BUTTON)

    def perform_forgot_password(self, email):
        """Perform forgot password request"""
        self.click_element(*self.FORGOT_PASSWORD_LINK)
        self.input_text(*self.RECOVERY_EMAIL_INPUT, email)
        self.click_element(*self.SUBMIT_RECOVERY_BUTTON)

    def get_recovery_success_message(self):
        """Get the success message after password recovery request"""
        return self.get_text(*self.RECOVERY_SUCCESS_MESSAGE)

    def get_error_message(self):
        """Get the error message if any"""
        return self.get_text(*self.ERROR_MESSAGE)

    def get_snackbar_message(self):
        """Get the snackbar message if any"""
        return self.get_text(*self.SNACKBAR_MESSAGE) 