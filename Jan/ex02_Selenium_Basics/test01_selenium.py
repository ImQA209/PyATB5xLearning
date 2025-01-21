import time

from selenium import webdriver
import allure
import pytest


@allure.title("open the app vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https:/app.vwo.com")
    driver.maximize_window()
    print(driver.session_id)
    time.sleep(15)
