import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page_v2 import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read("config.ini")

        # Lấy URL trang login từ file config
        self.login_url = config["app"]["login_url"]

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def test_invalid_login_with_wrong_password(self):
        """Test đăng nhập với mật khẩu sai"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("wrong_password")
        login_page.click_login()

        # Kiểm tra thông báo lỗi
        error_message = login_page.get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_invalid_login_with_wrong_email(self):
        """Test đăng nhập với email sai"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("wrong_email@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Kiểm tra thông báo lỗi
        error_message = login_page.get_error_message()
        self.assertIn("Invalid credentials", error_message)

    def test_empty_login_fields(self):
        """Test đăng nhập với các trường để trống"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Không nhập gì cả, click thẳng vào nút đăng nhập
        login_page.click_login()

        # Kiểm tra thông báo lỗi cho email trống
        email_error = login_page.get_email_error_message()
        self.assertEqual("Ban chua nhap dia chi email", email_error)

        # Kiểm tra thông báo lỗi cho mật khẩu trống
        password_error = login_page.get_password_error_message()
        self.assertEqual("Ban chua nhap mat khau", password_error)

    def test_invalid_email_format(self):
        """Test đăng nhập với email không đúng định dạng"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập email không có ký tự @
        login_page.enter_username("213123")
        login_page.click_login()

        # Kiểm tra thông báo lỗi định dạng email
        email_error = login_page.get_email_error_message()
        self.assertEqual("Định dạng phải có '@' trong chuỗi", email_error)

    def test_password_minimum_length(self):
        """Test đăng nhập với mật khẩu ít hơn 16 ký tự"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("test@gmail.com")
        # Nhập mật khẩu chỉ có 8 ký tự
        login_page.enter_password("12345678")
        login_page.click_login()

        # Kiểm tra thông báo lỗi về độ dài mật khẩu
        password_error = login_page.get_password_error_message()
        self.assertEqual("Yeu cau toi thieu 16 ky tu", password_error)

    def test_email_minimum_length(self):
        """Test đăng nhập với email ít hơn 6 ký tự"""
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập email chỉ có 5 ký tự
        login_page.enter_username("a@b.c")
        login_page.click_login()

        # Kiểm tra thông báo lỗi về độ dài email
        email_error = login_page.get_email_error_message()
        self.assertEqual("Email phai co toi thieu 6 ky tu", email_error)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
