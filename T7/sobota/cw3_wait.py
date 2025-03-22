from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# as dodaje nam alias danej rzeczy

# inicjalizacja przegladarki chrome
driver = webdriver.Chrome()

# 
driver.implicitly_wait(10)

url = "https://www.w3schools.com/"

# pobranie konretnego adresu w przegladarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

#ciasteczka
time.sleep(3)
accept_cookies2 = driver.find_element("id", "accept-choices")
accept_cookies2.click()
# driver.find_element("id", "accept-choices").click()

menu =driver.find_element("id", "navbtn_tutorials")
menu.click()
# webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# zbadaj -> copy -> copy xpath
learnHTML = driver.find_element('xpath', '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
learnHTML.click()

#expllicitly wait - czekamy na konkretny element
wait = WebDriverWait(driver, 10, 0.5)

# warunek oczekiwania
wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
# ewentualnie:
#   lambda x:
#   wait.until(len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))

# menu - 'input types'
menuInput = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')
menuInput.click()


time.sleep(500)

driver.quit()