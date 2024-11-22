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

    def test_01_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()
        login_page.check_error_message()
        

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def test_02_login_with_invalid_password(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin12345")
        login_page.click_login()
        login_page.check_error_message()

    def test_03_login_with_unregistered_username(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin11111111@gmail.com")
        login_page.enter_password("admin12345")
        login_page.click_login()
        login_page.check_error_message()

    def test_04_login_with_empty_username_and_password_fields(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()
        login_page.check_error_message()  

    def test_05_login_with_invalid_email(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("P@1")
        login_page.enter_password("admin123")
        login_page.click_login()
        login_page.check_error_message() 

    def test_06_login_with_empty_email_field(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("")
        login_page.enter_password("admin123")
        login_page.click_login()
        login_page.check_error_message() 

    def test_07_login_with_empty_password_field(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("")
        login_page.click_login()
        login_page.check_error_message() 

    def test_08_valid_login_with_user_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("phuong3112@gmail.com")
        login_page.enter_password("123")
        login_page.click_login()
        login_page.check_error_message()
        

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

