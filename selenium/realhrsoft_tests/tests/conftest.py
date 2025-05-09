import pytest
from realhrsoft_tests.utils.webdriver_factory import WebDriverFactory
from realhrsoft_tests.config.config import BASE_URL, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT

@pytest.fixture(scope="function")
def driver():
    """Fixture to create and manage webdriver instance"""
    driver = WebDriverFactory.get_driver()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.maximize_window()
    driver.get(BASE_URL)
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """Fixture to provide base URL"""
    return BASE_URL 