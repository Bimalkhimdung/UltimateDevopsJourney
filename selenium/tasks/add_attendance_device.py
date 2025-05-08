from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.switch_org import switch_org
from utils.login_as_user import login 
import logging
import time 
def add_attendance_device():
    driver=None
    try:
        driver=switch_org()
        if not driver:
            raise ValueError("Driver initialization failed")
        logging.info("Successfully initialized driver")
        try:
            current_url = driver.current_url
            logging.info(f"Current URL: {current_url}")
        except Exception as e:
            logging.error(f"Driver session check failed: {str(e)}")
            raise ValueError("Invalid driver session")
        settings_xpath = "//div[contains(@class, 'v-list-item__title') and contains(., 'Settings')]"
        add_device = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, settings_xpath))
        )
        driver.execute_script("arguments[0].click();", add_device)
        time.sleep(2)
        add_device.click()
        time.sleep(2)
    except Exception as e:
        logging.error(f"Error in add_attendance_device: {str(e)}")
    finally:
        if driver:
            driver.quit()
        
if __name__ == "__main__":
    add_attendance_device()