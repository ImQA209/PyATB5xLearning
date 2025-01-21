from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By


def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()