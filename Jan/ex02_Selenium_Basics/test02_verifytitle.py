import time
import allure
from selenium import webdriver


@allure.title("verify the tittle")
@allure.description("To verify the vwo login tittle")
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
