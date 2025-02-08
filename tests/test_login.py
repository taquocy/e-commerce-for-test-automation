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

    def test_valid_login_with_admin_account(self):
        """Đăng nhập thành công với tài khoản admin"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        self.assertTrue(admin_page.check_admin_page_display(), "Không vào được trang admin!")

    def test_valid_login_with_user_account(self):
        """Đăng nhập thành công với tài khoản user"""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("user@gmail.com")
        login_page.enter_password("Y649394$y")
        login_page.click_login()

        # Kiểm tra xem user có đăng nhập thành công không (tùy theo giao diện)
        self.assertTrue(login_page.check_success_login(), "User không đăng nhập thành công!")

    def test_user_cannot_login_with_invalid_password(self):
        """Người dùng không thể đăng nhập với mật khẩu sai"""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()

        login_page.enter_username("ngominh011@gmail.com")
        login_page.enter_password("1235")
        login_page.click_login()

        # Kiểm tra xem có hiển thị lỗi không
        self.assertTrue(login_page.check_email_error(), "Không hiển thị lỗi khi nhập sai mật khẩu!")

    def test_login_with_unregistered_username(self):
        """Người dùng không thể đăng nhập với email chưa đăng ký"""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()

        login_page.enter_username("noname@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login()

        # Kiểm tra lỗi hiển thị
        self.assertTrue(login_page.check_email_error(), "Không hiển thị lỗi khi email chưa đăng ký!")

    def tearDown(self):
        """Đóng trình duyệt sau khi chạy test"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
