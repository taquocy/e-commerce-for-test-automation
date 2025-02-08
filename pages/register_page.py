from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        #####
        # Xác định các phần tử trên trang login
        self.menu_login =  (By.XPATH, "//a[@href='/signin']/button")
        self.email_field = (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH,"//input[@name='password']")

    def open_login_form(self):
        self.driver.find_element(*self.menu_login).click()
        