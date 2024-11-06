import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import RegisterPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang register từ file config
        self.Register_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.Register_url)  # Sử dụng URL từ file config

    def test_valid_register_with_admin_account(self):
        login_page = RegisterPage(self.driver)

        login_page.open_register_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

