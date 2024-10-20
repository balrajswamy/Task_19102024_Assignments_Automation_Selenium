import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@allure.step("Open registration page")
@allure.title("TestCase #2")
@allure.description("Navigating a URL")
def open_registration_page(driver):
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

@allure.title("TestCase #2 using XPATH")
@allure.description("Filling a form by finding elements xpath")
@allure.step("Fill registration form with user data: {first_name}, {last_name}")
def fill_registration_form(driver, first_name, last_name, email, telephone, password):
    driver.find_element(By.XPATH, '//input[@name="firstname"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys(last_name)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@name="telephone"]').send_keys(telephone)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@name="confirm"]').send_keys(password)
    driver.find_element(By.NAME, "agree").click()

@allure.description("Submitting form")
@allure.step("Submit registration form")
def submit_registration(driver):
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

@allure.title("User Registration form is processing")
@allure.description("Form validation is going here")
@allure.description("Valid Registration")
def test_registration(setup):
    driver = setup
    #open_registration_page(driver)
    fill_registration_form(driver, "John", "Doe", "john@example.com", "1234567890", "password123")
    #submit_registration(driver)

    # Verifying the registration is successful

    #assert "Your Account Has Been Created!" in success_message
    try:
        success_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]").text
        assert "Your Account Has Been Created!" in success_message, "Registration failed"
    except:
        # //*[@id="account-register"]/div[1]/text()
        # print("alert",driver.find_element(By.XPATH,'//div[contains(@class,"alert-danger")]/text()').text)

        assert "Warning: E-Mail Address is already registered!"
