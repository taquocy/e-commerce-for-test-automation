import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


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

    def perform_login_test(self, email, password, expected_success=True):
        """Thực hiện kiểm tra đăng nhập với email và mật khẩu cho trước"""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login()
        
        if expected_success:
            # Kiểm tra xem có vào được trang Admin không
            admin_page = AdminPage(self.driver)
            admin_page.check_admin_page_display()
        else:
            # Kiểm tra hiển thị thông báo lỗi
            login_page.check_login_error_message()

    def test_valid_login_with_admin_account(self):
        """Kiểm tra đăng nhập với tài khoản admin"""
        self.perform_login_test("superadmin@gmail.com", "admin123")
    
    def test_valid_login_with_nam_account(self):
        """Kiểm tra đăng nhập với tài khoản nam@gmail.com"""
        self.perform_login_test("nam@gmail.com", "nam123")

    def test_invalid_login_with_wrong_password(self):
        """Kiểm tra đăng nhập với mật khẩu sai"""
        self.perform_login_test("nam@gmail.com", "wrongpassword", expected_success=False)
    
    def test_invalid_login_with_nonexistent_user(self):
        """Kiểm tra đăng nhập với tài khoản không tồn tại"""
        self.perform_login_test("nonexistent@gmail.com", "randompass", expected_success=False)
    
    def test_invalid_login_with_empty_fields(self):
        """Kiểm tra đăng nhập với trường trống"""
        self.perform_login_test("", "", expected_success=False)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))