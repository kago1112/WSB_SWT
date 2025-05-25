# page object model
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'
        self.after_login_url = 'https://www.saucedemo.com/inventory.html'
    
    def open(self):
        self.driver.get('https://www.saucedemo.com')
    
    def print_page_info(self):
        print(f"Nazwa strony: {self.driver.title}")
        print(f"URL strony: {self.driver.current_url}")

    def get_current_url(self):
        return self.driver.current_url
    
    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.username_field_id)
        field.clear()    # clear the field before entering text
        field.send_keys(username)    # enter the username
    
    def enter_password(self, password):
        field = self.driver.find_element(By.ID, self.password_field_id)
        field.clear()    # clear the field before entering text
        field.send_keys(password)    # enter the password
    
    def click_login(self):
        button = self.driver.find_element(By.NAME, self.login_button_name)
        button.click()    # click the login button

