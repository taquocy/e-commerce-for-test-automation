from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        # Xác định các phần tử trên trang login
        self.email = (By.XPATH, "//input[@name='email']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.confirm_password = (By.XPATH, "//input[@name='confirmPassword']")
        self.register_button = (By.XPATH, "//button[@type='submit']")


