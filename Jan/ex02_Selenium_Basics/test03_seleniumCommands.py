import allure
from selenium import webdriver
import pytest


@allure.title("Verify the vmo login commends")
@allure.description("verifying the cmds")
def test_login_vmo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.current_url)
    print(driver.title)
    print(driver.page_source)
