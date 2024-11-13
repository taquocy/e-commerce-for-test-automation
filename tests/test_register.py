import unittest
import configparser
import HtmlTestRunner
import sys
import os
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()

        # Kiểm tra nếu file config.ini tồn tại
        config_file = 'config.ini'
        if not os.path.exists(config_file):
            self.fail(f"File cấu hình {config_file} không tồn tại.")
        
        config.read(config_file)

        # Lấy URL của trang đăng ký từ config
        self.register_url = config['app']['register_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.register_url)  # Điều hướng đến trang đăng ký

    def generate_random_email(self):
        """Tạo email ngẫu nhiên để tránh trùng lặp trong kiểm thử."""
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = "email.com"
        return f"{username}@{domain}"

    def test_valid_register_new_user(self):
        register_page = RegisterPage(self.driver)

        # Mở form đăng ký và điền thông tin
        register_page.open_register_form()

        random_email = self.generate_random_email()  # Tạo email ngẫu nhiên
        register_page.enter_email(random_email)
        register_page.enter_password("password123")
        register_page.enter_confirm_password("password123")
        register_page.click_register()

        # Kiểm tra hiển thị thông báo đăng ký thành công
        success_message = register_page.check_success_message()
        self.assertIsNotNone(success_message, "Thông báo thành công không hiển thị.")
        self.assertIn("Đăng ký thành công", success_message, "Thông báo không đúng.")

    def tearDown(self):
        """Đóng trình duyệt sau mỗi bài test."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
