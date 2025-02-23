import unittest
import configparser

import HtmlTestRunner # type: ignore
import sys
import os


# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


config = configparser.ConfigParser()

config_path = os.path.abspath("config.ini")  # Đảm bảo đường dẫn đúng
print(f"🔍 Đang đọc file: {config_path}")  # In ra đường dẫn file để kiểm tra

config.read(config_path)

# Kiểm tra nội dung đọc được
print("📌 Các sections tìm thấy:", config.sections())

if 'app' not in config:
    raise ValueError("❌ Không tìm thấy section [app] trong config.ini")

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_01_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("ducaudi38@gmail.com")
        login_page.enter_password("12345678")
        login_page.click_login()
        
        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def test_02_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("user@example.com")
        login_page.enter_password("WrongPass")
        login_page.click_login()
        login_page.check_error_message()

    def test_03_unregistered_email(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("unknown@example.com")
        login_page.enter_password("AnyPass")
        login_page.click_login()
        login_page.check_error_message()

    def test_04_empty_email_and_password(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()
        login_page.check_error_message()

    def test_05_invalid_email_format(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("userexample.com")
        login_page.enter_password("AnyPass")
        login_page.click_login()
        login_page.check_error_message()

    def test_06_sql_injection_attempt(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("admin' OR 1=1 --")
        login_page.enter_password("AnyPass")
        login_page.click_login()
        login_page.check_error_message()

    def test_07_xss_attempt(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("<script>alert(1)</script>")
        login_page.enter_password("AnyPass")
        login_page.click_login()
        login_page.check_error_message()

    def test_08_case_sensitive_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("USER@example.com")
        login_page.enter_password("VALIDPASS123")
        login_page.click_login()
        login_page.check_error_message()

    def test_09_locked_account(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("lockeduser@example.com")
        login_page.enter_password("ValidPass123")
        login_page.click_login()
        login_page.check_error_message()

    def test_10_remember_me_enabled(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("user@example.com")
        login_page.enter_password("ValidPass123")
        login_page.click_remember_me()
        login_page.click_login()
        
        # Đóng trình duyệt và mở lại để kiểm tra trạng thái đăng nhập
        self.driver.quit()
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)
        
        login_page.check_remember_me()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
