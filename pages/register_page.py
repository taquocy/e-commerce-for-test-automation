from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang đăng ký
        self.menu_register = (By.XPATH, "//a[@href='/signup']/button")  # Nút mở form đăng ký
        self.email_field = (By.XPATH, "//input[@name='email']")  # Trường nhập email
        self.password_field = (By.XPATH, "//input[@name='password']")  # Trường nhập password
        self.confirm_password_field = (By.XPATH, "//input[@name='confirm_password']")  # Nhập lại password
        self.register_button = (By.XPATH, "//button[@type='submit']")  # Nút đăng ký

    def open_register_form(self):
        """Mở form đăng ký"""
        self.driver.find_element(*self.menu_register).click()

    def enter_email(self, email):
        """Nhập email"""
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        """Nhập mật khẩu"""
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        """Nhập lại mật khẩu"""
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_register(self):
        """Nhấn nút đăng ký"""
        self.driver.find_element(*self.register_button).click()
