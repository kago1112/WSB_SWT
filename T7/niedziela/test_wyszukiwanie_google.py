import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# dekorator
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google_search(driver):
    url = "https://www.google.com"
    driver.get(url)
    
    assert "Google" in driver.title

    accept_cookies = driver.find_element("id", "L2AGLb")
    accept_cookies.click()

    search_text = driver.find_element("name", "q")
    search_text.send_keys("Pogoda")
    search_text.send_keys(Keys.ENTER)

    time.sleep(30)

    results = driver.find_elements("css_selector", "h3")
    print(results)