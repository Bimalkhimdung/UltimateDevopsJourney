from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from realhrsoft_tests.config.config import BROWSER, HEADLESS
import platform

class WebDriverFactory:
    @staticmethod
    def get_driver():
        """Initialize and return the appropriate webdriver based on configuration"""
        if BROWSER.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            if HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            # Check if running on Apple Silicon
            if platform.processor() == 'arm':
                options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                options.add_argument('--disable-gpu')
            
            service = ChromeService('/usr/local/bin/chromedriver')
            return webdriver.Chrome(service=service, options=options)
        
        elif BROWSER.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            if HEADLESS:
                options.add_argument('--headless')
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        elif BROWSER.lower() == 'edge':
            options = webdriver.EdgeOptions()
            if HEADLESS:
                options.add_argument('--headless')
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}") 