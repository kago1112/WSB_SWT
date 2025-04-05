import pytest
import time
from page_object_pattern.pages.google_search import SearchPage
from page_object_pattern.pages.google_result import ResultPage
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# test
def test_google_serach(driver):
    # utworzenie obiekt klasy search page
    search_page = SearchPage(driver)
    search_page.open()

    assert "Google" in driver.title

    search_page.accept_cookies()

    search_page.search("Najlepsza kawa w Polsce")

    time.sleep(20)

    # utworzenie obiektu klasy result
    result_page = ResultPage(driver)

    results = result_page.get_results()
    assert len(results) > 0, "Niestety, nic nie ma"

