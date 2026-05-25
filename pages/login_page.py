from pages.inventory_page import InventoryPage

class LoginPage :
    def __init__(self, page) :
        self.page = page 

        self.username_input = page.locator("[data-test = 'username']")

        self.password_input = page.locator("[data-test = 'password']")
        self.login_button = page.locator("[data-test = 'login-button']")
    #   another meathod  # self.submit_button = page.get_by_role("button", name="Search")
        


        self.error_message = page.locator("[data-test = 'error']")


    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self , username , password ):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)
    
    def get_error(self):
        return self.error_message.inner_text()