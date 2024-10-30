from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.email_field =  (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH, "//input[@name='password']")


    def enterEmailField(self,value):
        self.driver.find_element(*self.email_field).send_keys(value)
