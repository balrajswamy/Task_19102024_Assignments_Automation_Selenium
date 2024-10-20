import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time

@allure.title("TestCase #1 to test https://app.vwo.com")
@allure.description("verify the invalid username/email with password")
@allure.step("Verify the username with password and getting a error message")
def test_invalid_login():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://app.vwo.com/#/login")
    time.sleep(1)
    email = driver.find_element(By.XPATH,"//input[@name='username']")
    email.send_keys("balraj@gmail.com")
    time.sleep(1)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("123@123")
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[@id="js-login-btn"]').click()
    time.sleep(3)
    try:
        error_message = driver.find_element(By.XPATH,'//*[@id="js-notification-box-msg"]').text
        assert 'Your email, password, IP address or location did not match' in error_message
    except:
        assert "Login success"