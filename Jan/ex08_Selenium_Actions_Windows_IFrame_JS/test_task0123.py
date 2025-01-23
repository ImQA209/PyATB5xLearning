import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from allure_commons.types import AttachmentType


@allure.title("Action class")
@allure.description("Verify the action class")
def test_verifyAction():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    FromCity = driver.find_element(By.XPATH, "//*[@data-testid='to-testID-origin']")
    actions = ActionChains(driver=driver)
    actions.move_to_element(FromCity).click().send_keys("kol").perform()
    time.sleep(2)
    ToCity = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-destination']")
    actions = ActionChains(driver=driver)
    actions.move_to_element(ToCity).click().send_keys("Blr").perform()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="test_verify_action_spicejet-screenshot",
                  attachment_type=AttachmentType.PNG)
