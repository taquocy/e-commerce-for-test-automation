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

    # TC01: Verify that the user can access the "Register" creation page
    def test_open_register_page(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.check_register_success()

    # TC02: Verify valid registration
    def test_valid_registration(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_password("ValidPassword123")
        register_page.enter_confirm_password("ValidPassword123")
        register_page.click_register()
        register_page.check_register_success()

    # TC03: Ensure the "Email" field is required
    def test_email_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_password("123456")
        register_page.enter_confirm_password("123456")
        register_page.click_register()
        register_page.check_form_error("E-mail field is required")

    # TC04: Ensure the "Password" field is required
    def test_password_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_confirm_password("123456")
        register_page.click_register()
        register_page.check_form_error("Password field is required")

    # TC05: Ensure the "Password Confirm" field is required
    def test_confirm_password_field_is_required(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_password("123456")
        register_page.click_register()
        register_page.check_form_error("Password Confirm field is required")

    # TC06: Verify invalid 'Email' format
    def test_invalid_email_format_is_rejected(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam.com")
        register_page.enter_password("123456")
        register_page.enter_confirm_password("123456")
        register_page.click_register()
        register_page.check_form_error("Invalid email")

    # TC07: Verify 'Email' has been registered
    def test_register_with_existing_email(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("abc@abc.abc")  # Email đã đăng ký trước
        register_page.enter_password("12345678")
        register_page.enter_confirm_password("12345678")
        register_page.click_register()
        register_page.check_form_error("This e-mail already using.")

    # TC08: Verify password and confirm password do not match
    def test_password_and_confirm_password_mismatch(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_password("123456")
        register_page.enter_confirm_password("654321")
        register_page.click_register()
        register_page.check_form_error("Password does not match")

    # TC09: Verify invalid password (password is too short)
    def test_invalid_password_too_short(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_password("ab")
        register_page.enter_confirm_password("ab")
        register_page.click_register()
        register_page.check_form_error("Invalid Password")

    # TC10: Verify password contains spaces
    def test_password_with_spaces(self):
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("hainam@gmail.com")
        register_page.enter_password("abc def")
        register_page.enter_confirm_password("abc def")
        register_page.click_register()
        register_page.check_form_error("Invalid Password")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
