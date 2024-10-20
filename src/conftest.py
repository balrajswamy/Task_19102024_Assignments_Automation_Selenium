import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="function")
def setup(request):
    with allure.step("Initializing WebDriver"):
        driver = webdriver.Chrome()  # Initialize the browser (Chrome)
        driver.maximize_window()

    with allure.step("Navigating to the registration page"):
        driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Teardown function to close the browser after the test
    def teardown():
        with allure.step("Closing the WebDriver"):
            driver.quit()

    # Registering the teardown to run after the test
    #request.addfinalizer(teardown)

    return driver  # Return the driver instance to be used in tests
