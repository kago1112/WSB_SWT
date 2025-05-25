# i co to kurwa ma niby robić


from selenium import webdriver
from pom import LoginPage
from selenium.webdriver.common.by import By
from time import sleep

#testowanie strony logowania
def test_login_page():
    driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    page = LoginPage(driver)  # Create an instance of the LoginPage class
    page.open() # Open the login page
    page.print_page_info()  # Print the page information
    page.enter_username('standard_user')  # Enter username
    page.enter_password('secret_sauce')  # Enter password
    page.click_login()  # Click the login button
    sleep(5)  # Wait for 5 seconds to observe the result
    page.print_page_info()  # Print the page information again
    try:
        assert page.get_current_url() == page.after_login_url
    except AssertionError:
        print('Asercja nie powiodła się.')
    else:
        print('Asercja powiodła się.')
    finally:
        print('Po asercji.')

    driver.quit()  # Close the browser