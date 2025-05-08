from selenium import * 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.switch_org import switch_org
import time 

def add_attendance_device():
    print("enter in to add_attendance_device")
    switch_org()
    
    time.sleep(2)

    
    