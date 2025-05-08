from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Set up Chrome driver
def login():
  """
  Logs into the RealHRSoft system using the credentials provided in the .env file.

  If the environment variables LOGIN_USER and LOGIN_PASSWORD are not set, the function will
  use the default values of 'admin@realhrsoft.com' and 'RealHRsoft@456' respectively.

  If the function is unable to login, it will raise an exception with a message indicating
  the error.

  Returns:
    The selenium webdriver object that was used to login.
  """
  service = Service('/usr/local/bin/chromedriver') 
  options = Options()
  options.add_argument("--start-maximized")
  driver = webdriver.Chrome(service=service, options=options)
  try:
    driver.get("https://stage.realhrsoft.com/account/login")  
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "id_email"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "id_password"))
    )
    # Locate the username and password fields
    username_field = driver.find_element(By.ID, "id_email")  
    password_field = driver.find_element(By.ID, "id_password")  

    username = os.environ.get('LOGIN_USER','sujan.sitikhu@aayulogic.com')
    password = os.environ.get('LOGIN_PASSWORD','RealHRsoft@456')

    if not username or not password:
            raise password("Username or password not found in .env file")

    # Input your credentials
    username_field.send_keys(username) 
    password_field.send_keys(password) 

    # Locate and click the login button
    login_button = driver.find_element(By.ID, "logInButton") 

    login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logInButton")))

    login_button.click()
    driver.implicitly_wait(5)  
    return driver
  except Exception as e:
    print(f"An Error occurred while login into the system: {e}")
    #driver.quit()
    raise
if __name__ == "__main__":
    login()
