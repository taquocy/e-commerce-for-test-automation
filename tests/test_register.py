from selenium.webdriver.common.by import By
import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang register từ file config
        self.register_url = config['app']['register_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.register_url)  # Sử dụng URL từ file config

    # Verify that the user can access the "Sign Up" page
    def test_open_register_page(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.check_load_register_page_success()


    # Ensure the "E-mail" field is required
    def test_email_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.click_register()
        register_page.check_form_input_error("E-mail field is required")

    # Ensure the "Password" field is required
    def test_password_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tuan@gmail.com")
        register_page.enter_password_confirm("123456")
        register_page.click_register()
        register_page.check_form_input_error("Password field is required")

    # Ensure the "Password Confirm" field is required
    def test_confirm_password_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tuan@gmail.com")
        register_page.enter_password("123456")
        register_page.click_register()
        register_page.check_form_input_error("Password Confirm field is required")

    # Verify that invalid email format is rejected
    def test_invalid_email_format_is_rejected(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tuan@email")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.click_register()
        register_page.check_form_input_error("email must be a valid email")    

    # Verify that the password and confirm password fields match
    def test_the_password_and_confirm_password_fields_match(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tuantest@gmail.com")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123458")
        register_page.click_register()
        register_page.check_form_input_error("the password and confirm password do not match")

    # Verify that the system rejects an already registered email
    def test_register_with_existing_email(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tranductuan291018@gmail.com")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.click_register()
        register_page.check_form_input_error("This e-mail already using")

    # Verify that the system rejects an overly long email input
    def test_system_rejects_an_overly_long_email_input(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tranductuandsdkhasjkdhjkshdjkas29101866+5564545684554564@gmail.com")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.click_register()
        register_page.check_form_input_error("The email exceeds the maximum allowed length")

    # Verify that the system rejects a password with less than 3 characters
    def test_the_system_rejects_a_password_with_less_than_3_characters(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("tuan@gmail.com")
        register_page.enter_password("12")
        register_page.enter_password_confirm("12")
        register_page.click_register()
        register_page.check_form_input_error("password length must be at least 3 characters long")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
