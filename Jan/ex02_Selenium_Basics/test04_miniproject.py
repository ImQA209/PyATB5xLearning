import allure
import pytest
from selenium import webdriver


@allure.title("Verify that strings in homepage")
@allure.description(" To verify whether the strings available or not")
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text found and Test case is passed")
    
    else:
        print("Text not found")
        pytest.fail("Text not found in page")
