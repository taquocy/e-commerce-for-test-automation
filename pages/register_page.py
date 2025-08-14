from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        self.menu_register =  (By.XPATH, "//a[@href='/signup']/button")
        self.email_input = (By.NAME, "email")  
        self.password_input = (By.NAME, "password")  
        self.confirm_password_input = (By.NAME, "passwordConfirm")  
        self.register_button = (By.XPATH, "//button[@type='submit']")  

    def open_registration_form(self):
        self.driver.find_element(*self.menu_register).click()
    
    def enter_email(self, username):
        self.driver.find_element(*self.email_input).send_keys(username)

    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    def enter_confirm_password(self, password):
        self.driver.find_element(*self.confirm_password_input).send_keys(password)

    
    def click_register(self):
        self.driver.find_element(*self.register_button).click()