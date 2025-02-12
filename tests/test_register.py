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

        # Lấy URL trang đăng ký từ file config
        self.register_url = config['app']['register_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.register_url)

    def test_01_valid_register(self):
        """Test đăng ký hợp lệ với tài khoản mới"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("newuser@example.com")
        register_page.enter_password("StrongPassword123!")
        register_page.enter_password_confirm("StrongPassword123!")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertIsNone(error_message, "Expected successful registration, but found an error.")

    def test_02_register_with_existing_email(self):
        """Test đăng ký với email đã tồn tại"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("existinguser@gmail.com")
        register_page.enter_password("Password123!")
        register_page.enter_password_confirm("Password123!")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "email_exists", "Expected 'email already exists' error.")

    def test_03_register_with_invalid_email(self):
        """Test đăng ký với email không hợp lệ"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("invalid-email")
        register_page.enter_password("Password123!")
        register_page.enter_password_confirm("Password123!")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "invalid_email", "Expected 'invalid email' error.")

    def test_04_register_with_weak_password(self):
        """Test đăng ký với mật khẩu yếu"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("weakpass@example.com")
        register_page.enter_password("123")
        register_page.enter_password_confirm("123")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "weak_password", "Expected 'password too weak' error.")

    def test_05_register_with_mismatched_passwords(self):
        """Test đăng ký với mật khẩu không khớp"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("mismatch@example.com")
        register_page.enter_password("Password123!")
        register_page.enter_password_confirm("Password456!")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "password_mismatch", "Expected 'passwords do not match' error.")

    def test_06_register_with_empty_fields(self):
        """Test đăng ký khi bỏ trống tất cả các trường"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("")
        register_page.enter_password("")
        register_page.enter_password_confirm("")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "chua_nhap_email", "Expected 'blank email' error.")

    def test_07_register_with_empty_password(self):
        """Test đăng ký khi bỏ trống mật khẩu"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("test@example.com")
        register_page.enter_password("")
        register_page.enter_password_confirm("")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "chua_nhap_password", "Expected 'blank password' error.")

    def test_08_register_with_empty_password_confirm(self):
        """Test đăng ký khi bỏ trống xác nhận mật khẩu"""
        register_page = RegisterPage(self.driver)
        register_page.open_register_form()
        register_page.enter_email("test@example.com")
        register_page.enter_password("ValidPassword123!")
        register_page.enter_password_confirm("")
        register_page.click_register()
        
        error_message = register_page.check_error_message()
        self.assertEqual(error_message, "chua_nhap_password_confirm", "Expected 'blank password confirm' error.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

    