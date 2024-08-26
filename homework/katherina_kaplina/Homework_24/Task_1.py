from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def test_product_in_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@href="prod.html?idp_=1" and @class="hrefch"]'))
    )

    product = driver.find_element(
        By.XPATH, '//*[@href="prod.html?idp_=1" and @class="hrefch"]'
    )
    product_name = product.text

    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.btn-success')))
    driver.find_element(By.CSS_SELECTOR, '.btn-success').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())

    alert = Alert(driver)
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    driver.find_element(By.ID, 'cartur').click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.success')))
    product_name_from_cart = driver.find_element(By.XPATH, '//*[@class="success"]/child::td[2]').text

    assert product_name_from_cart == product_name
