class SearchPage:
    def __init__(self, driver):
        self.accept_cookies_button = ("id", "L2AGLb")
        self.search_box = ("name", "q")

    def open(self):
        self.driver.get("https://www.google.com")
    
    def accept_cookies(self):
        accept_cookies = self.driver.find_element(*self.accept_cookies_button)
        accept_cookies.click()

    def search(self, query):
        search_box = driver.find_element("name", "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)