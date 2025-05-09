from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def find_element(self, by, value):
        """Find element with explicit wait"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {value}")
            raise

    def click_element(self, by, value):
        """Click element with explicit wait"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
        except TimeoutException:
            self.logger.error(f"Element not clickable: {value}")
            raise

    def input_text(self, by, value, text):
        """Input text with explicit wait"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.logger.error(f"Element not found for input: {value}")
            raise

    def get_text(self, by, value):
        """Get text from element with explicit wait"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            return element.text
        except TimeoutException:
            self.logger.error(f"Element not found for text: {value}")
            raise

    def take_screenshot(self, name):
        """Take screenshot and save it"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        filepath = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(filepath)
        self.logger.info(f"Screenshot saved: {filepath}")
        return filepath 