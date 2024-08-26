from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    sleep(6)


def test_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product = driver.find_element(By.XPATH, '//*[@class="product-item-link"][1]')
    compare_button = driver.find_element(By.XPATH, '//*[@class="action tocompare"][1]')

    first_product_name = first_product.text
    ActionChains(driver).move_to_element(first_product).click(compare_button).perform()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.product-item.odd.last strong a')))

    assert driver.find_element(By.CSS_SELECTOR, '.product-item.odd.last strong a').text == first_product_name
