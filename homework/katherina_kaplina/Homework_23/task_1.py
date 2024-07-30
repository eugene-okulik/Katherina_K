from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


def test_hw_1(driver):
    input_data = 'test'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(f'\nYour input was {result_text.text}')
    assert result_text.text == input_data
