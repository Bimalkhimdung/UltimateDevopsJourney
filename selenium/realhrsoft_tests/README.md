# Selenium Test Framework for RealHRsoft

This is a Selenium-based test automation framework for testing the RealHRsoft application. The framework is built using Python, Selenium WebDriver, and Pytest.

## Project Structure

```
selenium/
├── config/
│   └── config.py           # Configuration settings
├── pageobjects/
│   ├── base_page.py       # Base page object class
│   └── login_page.py      # Login page object
├── tests/
│   ├── conftest.py        # Pytest fixtures
│   └── test_login.py      # Login test cases
├── utils/
│   └── webdriver_factory.py # WebDriver initialization
├── test_data/
│   └── users.json         # Test data
└── requirements.txt       # Python dependencies
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
BASE_URL=https://your-application-url.com
BROWSER=chrome
HEADLESS=False
IMPLICIT_WAIT=10
PAGE_LOAD_TIMEOUT=30
```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test file:
```bash
pytest tests/test_login.py
```

To run tests with HTML report:
```bash
pytest --html=reports/report.html
```

## Features

- Page Object Model design pattern
- Configurable browser settings
- Support for multiple browsers (Chrome, Firefox, Edge)
- Screenshot capture on test failure
- HTML test reports
- Environment-based configuration
- Reusable test fixtures
- Data-driven testing support

## Adding New Tests

1. Create a new page object in the `pageobjects` directory
2. Create corresponding test file in the `tests` directory
3. Add test data in the `test_data` directory if needed
4. Run the tests using pytest

## Best Practices

- Use page objects for better maintainability
- Keep test data separate from test logic
- Use meaningful test names and descriptions
- Add appropriate assertions
- Handle exceptions properly
- Take screenshots on test failures
- Keep tests independent of each other 