from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_hw_3_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    selected_language = 'Python'

    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text(selected_language)

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == selected_language


def test_hw_3_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = driver.find_element(By.XPATH, '//button')
    start_button.click()

    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish')))
    result_text = driver.find_element(By.CSS_SELECTOR, '#finish')
    assert result_text.text == "Hello World!"
