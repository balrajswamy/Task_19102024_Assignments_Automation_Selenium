import pytest
from selenium.webdriver.common.by import By
import allure


@allure.title("Filling out registration form")
@allure.description("Filling a forum using xpath!")
@pytest.mark.smoke
def fill_registration_form(driver, first_name, last_name, email, telephone, password):
    # Fill out the registration form
    driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys(first_name)
    driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys(last_name)
    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys(telephone)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys(password)

    # Accept privacy policy
    driver.find_element(By.XPATH, "//input[@name='agree']").click()

    # Submit the form
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@allure.title("User Registration")
@allure.description("Valid Registration")
@pytest.mark.smoke
def test_valid_registration(setup):
    driver = setup

    # Example user data
    first_name = "John"
    last_name = "Doe"
    email = "johndoe123@example.com"
    telephone = "1234567890"
    password = "password123"

    with allure.step("Submitting valid registration form"):
        fill_registration_form(driver, first_name, last_name, email, telephone, password)

    # Verify that registration was successful
    success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1").text
    assert "Your Account Has Been Created!" in success_message, "Registration failed"


@allure.feature("User Registration")
@allure.story("Invalid Registration")
def test_invalid_registration(setup):
    driver = setup

    # Example invalid user data (e.g., missing password)
    first_name = "John"
    last_name = "Doe"
    email = "johndoe_invalid@example.com"
    telephone = "1234567890"
    password = ""  # Intentionally left blank

    with allure.step("Submitting invalid registration form"):
        fill_registration_form(driver, first_name, last_name, email, telephone, password)

    # Verify that an error message is displayed
    error_message = driver.find_element(By.XPATH, "//div[contains(@class,'alert-danger')]").text
    assert "Password must be between 4 and 20 characters!" in error_message, "Error message not displayed for invalid registration"

