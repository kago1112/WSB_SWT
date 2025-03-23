from selenium import webdriver
from selenium .webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC          #alias
from selenium.common.exceptions import TimeoutException
import time


def wait_for_button(driver, element_id):
    locator = ("id", element_id)

    locator_find = EC.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, 10, 0.5)

    return wait.until(locator_find, "Element nie pojawil sie po danym czasie")


driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"

driver.get(url)



try:
    login_button = wait_for_button(driver, "login-button")
    # jak wpiszesz "logi-button" to dostaniesz feedback "nie znaleziono elementu"
except TimeoutException:
    print("Nie znaleziono elementu")
    #HW - kliknac  ten przycisk
else:
    print("Znaleziono")
finally:
    time.sleep(5)
    driver.quit()
