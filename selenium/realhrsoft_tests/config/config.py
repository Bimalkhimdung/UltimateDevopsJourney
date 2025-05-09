import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base URL configuration
BASE_URL = os.getenv('BASE_URL', 'https://your-application-url.com')

# Browser configuration
BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'

# Timeout configurations
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

# Screenshot configuration
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports') 