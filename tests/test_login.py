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
        login_page.enter_username("ngominh011@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login()

        login_page.check_profile_page_display()

    def test_user_cannot_login_with_nonexistent_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("ngominh01@gmail.com")
        login_page.enter_password("1235")
        login_page.click_login()

        # Verify error message
        error_message = login_page.get_error_message()
        self.assertEqual(error_message, "The email address was not found.")

    def test_cannot_login_with_valid_email_and_invalid_password(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("ngominh011@gmail.com")
        login_page.enter_password("1235")
        login_page.click_login()

        # Verify error message
        error_message = login_page.get_error_message()
        self.assertEqual(error_message, "email or password not correct")

    def test_cannot_login_with_invalid_email_and_valid_password(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("ngominh01@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login()

        # Verify error message
        error_message = login_page.get_error_message()
        self.assertEqual(error_message, "The email address was not found.")

    def test_cannot_login_when_entering_case_sensitive_password(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        login_page.enter_username("ngominh01111@gmail.com")
        login_page.enter_password("MINH123")
        login_page.click_login()

        # Verify error message
        error_message = login_page.get_error_message()
        self.assertEqual(error_message, "The email address was not found.")

    def test_navigate_to_the_registration_page(self):
        login_page = LoginPage(self.driver)
        mess = "Signin"
        signup = "Signup"
        login_page.open_login_form()
        self.assertTrue(login_page.get_title(mess))
        login_page.open_register_form()
        self.assertTrue(login_page.get_title(signup))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

