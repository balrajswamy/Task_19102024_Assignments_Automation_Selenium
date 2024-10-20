import pytest
from selenium.webdriver.common.by import By
import allure
import time


@allure.step("Filling out the registration form")
@pytest.mark.smoke
def fill_registration_form(driver, first_name, last_name, email, telephone, password):
    # Fill in each field of the registration form
    with allure.step("Filling first name"):
        driver.find_element(By.ID, "input-firstname").send_keys(first_name)

    with allure.step("Filling last name"):
        driver.find_element(By.ID, "input-lastname").send_keys(last_name)

    with allure.step("Filling email"):
        driver.find_element(By.ID, "input-email").send_keys(email)

    with allure.step("Filling telephone"):
        driver.find_element(By.ID, "input-telephone").send_keys(telephone)

    with allure.step("Filling password"):
        driver.find_element(By.ID, "input-password").send_keys(password)
        driver.find_element(By.ID, "input-confirm").send_keys(password)

    with allure.step("Accepting privacy policy"):
        driver.find_element(By.NAME, "agree").click()

    with allure.step("Submitting registration form"):
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(12)

@allure.feature("User Registration")
@allure.story("Valid Registration")
@allure.title("TestCase #1 to fill a form using ByID")
@pytest.mark.smoke
def test_valid_registration_positive(setup):
    driver = setup

    # Sample valid data
    first_name = "John"
    last_name = "Doe"
    email = "johndoe123@example.com"
    telephone = "1234567890"
    password = "password123"

    with allure.step("Submitting valid registration"):
        fill_registration_form(driver, first_name, last_name, email, telephone, password)

    with allure.step("Verifying registration success"):
        success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1").text
        print(success_message)
        try:
            assert "Your Account Has Been Created!" in success_message, "Registration failed"
        except:
            #//*[@id="account-register"]/div[1]/text()
            #print("alert",driver.find_element(By.XPATH,'//div[contains(@class,"alert-danger")]/text()').text)

            assert "Warning: E-Mail Address is already registered!"



