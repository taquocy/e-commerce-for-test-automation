from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.username_input = (By.NAME, "email")  
        self.password_input = (By.NAME, "password") 
        self.login_button = (By.XPATH, "//button[@type='submit']")  

    def open_login_form(self):
        self.driver.find_element(*self.menu_login).click()
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

   
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
