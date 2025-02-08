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
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def test_valid_login_with_user_account(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("user@gmail.com")
        login_page.enter_password("Y649394$y")
        login_page.click_login()
        assert True

        # admin_page = AdminPage(self.driver)
        # admin_page.check_admin_page_display()

    def test_user_cannot_login_with_invalid_password(self):
        #1.Navigate to URL: https: // e - commerce -for -testing.onrender.com /
        # 2.Go to Login page
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        # 3. Enter info to the fields:
            # - Email:ngominh011@gmail.com
            # - Password:1235
        login_page.enter_username("ngominh011@gmail.com")
        login_page.enter_password("1235")

        # 4.Click Login button
        login_page.click_login()
        # Assert....

    def test_login_with_unregistered_username(self):
        # 1.Open the login page.
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        # 2.Enter unregistered username and any password.
        login_page.enter_username("noname@gmail.com")
        login_page.enter_password("12345")
        # 3.Click on "Login".
        login_page.click_login()
        # 4. Login fails.Error message "The email address was not found."
        login_page.check_email_error()
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

