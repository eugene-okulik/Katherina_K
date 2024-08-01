from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(1100, 1500)
    return chrome_driver


def test_hw_2(driver):
    input_data = {
        "first_name_data": "Kate",
        "last_name_data": "Test",
        "user_email_data": "kate@test.test",
        "user_mobile_data": "1234567890",
        "subject_data": "English",
        "user_address_data": "1st street Minsk"
    }

    driver.get('https://demoqa.com/automation-practice-form')

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys(input_data["first_name_data"])

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys(input_data["last_name_data"])

    user_email = driver.find_element(By.ID, 'userEmail')
    user_email.send_keys(input_data["user_email_data"])

    gender_radio = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-2"]')
    gender_radio.click()

    user_mobile = driver.find_element(By.ID, 'userNumber')
    user_mobile.send_keys(input_data["user_mobile_data"])

    subject = driver.find_element(By.ID, 'subjectsInput')
    subject.send_keys(input_data["subject_data"])
    subject.send_keys(Keys.ENTER)

    hobby_checkbox = driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-2"]')
    hobby_checkbox.click()

    user_address = driver.find_element(By.ID, 'currentAddress')
    user_address.send_keys(input_data["user_address_data"])

    state = driver.find_element(By.ID, 'state')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'state')))
    state.click()
    state_option = driver.find_element(By.XPATH, '//div[text()="NCR"]')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="NCR"]')))
    state_option.click()

    city = driver.find_element(By.ID, 'city')
    city.click()
    city_option = driver.find_element(By.XPATH, '//div[text()="Delhi"]')
    city_option.click()

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))

    table = driver.find_elements(By.CSS_SELECTOR, '.modal-content .table')

    for row in table:
        print(row.text)
