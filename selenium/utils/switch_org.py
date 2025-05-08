from selenium import * 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.login_as_user import login 
import time 
import logging
def switch_org():
    """
    Switch to the organization specified by the environment variable ORGANIZATION_NAME.
    If this variable is not set, the default organization is Aayulogic Pvt. Ltd.
    The function will log into the system and then switch to the desired organization.
    If any error occurs during the process, it will be logged and the script will exit.
    """
    #driver = login()
    try:
        driver = login()
        logging.info("Switching to Organization")
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.v-toolbar__content'))
        )
        dots_button = driver.find_element(By.CSS_SELECTOR, 'i.v-icon.notranslate.mdi.mdi-dots-vertical.theme--dark') 
        #print(f"Button HTML: {dots_button.get_attribute('outerHTML')} Clicked Successfully")
              
        dots_button.click()
        time.sleep(2)
        switch_organization = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-cy='main-dropdown-menu-item']//div[text()='Switch Organization']"))
        )
        switch_organization.click()
        import os
        org_name = os.environ.get('ORGANIGATION_NAME','Aayulogic Pvt. Ltd.')
    
        switch_org = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'v-card')]//div[contains(@class, 'v-card__text') and contains(text(), '{}')]".format(org_name)))
        )
        switch_org.click()
        time.sleep(2)   
        return driver
    except Exception as e:
        logging.error(f"Error occurred while switching organization: {e}")
        return None
    
    

if __name__ == "__main__":
    switch_org()

