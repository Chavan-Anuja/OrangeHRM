import pytest  # Import pytest for creating fixtures and configuring test options
from selenium.webdriver.chrome import webdriver  # Import Chrome WebDriver from selenium
from selenium import webdriver  # Import the main selenium webdriver module

# Create ChromeOptions object for headless browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")  # Run Chrome in headless mode


# Function to add command line option for selecting browser
def pytest_addoption(parser):
    parser.addoption("--browser")  # Add a command line option for browser selection


# Pytest fixture for setting up the WebDriver based on the selected browser
@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")  # Retrieve the browser option from command line
    if browser == "chrome":  # Check if the selected browser is Chrome
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    elif browser == "firefox":  # Check if the selected browser is Firefox
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()  # Initialize Firefox WebDriver
    elif browser == "edge":  # Check if the selected browser is Edge
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()  # Initialize Edge WebDriver
    else:  # Default to headless Chrome if no browser is specified or recognized
        print("Test Run - Headless")
        driver = webdriver.Chrome(options=chrome_options)  # Initialize headless Chrome WebDriver
    driver.maximize_window()  # Maximize the browser window
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Navigate to the login page
    yield driver  # Yield the WebDriver instance to be used in tests
    driver.quit()  # Quit the WebDriver after the test is completed


# Command to run pytest with specified options
# Pytest -v  --html=HTMLReports/myreport.html -n=2  --browser edge

# Pytest fixture for providing test data for login tests
@pytest.fixture(params=[  # Parameterize the fixture with multiple sets of test data
    ("Admin", "admin123", "Login_Pass"),  # Valid login credentials
    ("Admin1", "admin123", "Login_Fail"),  # Invalid username
    ("Admin", "admin1231", "Login_Fail"),  # Invalid password
    ("Admin1", "admin1231", "Login_Fail")  # Invalid username and password
])
def getDataForLogin(request):
    return request.param
