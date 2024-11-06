import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfileTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

    def test_update_profile_password_length_error_message(self):
        admin_page = AdminPage(self.driver)
        update_profile_page = admin_page.open_profile_page()
        update_profile_page = admin_page.open_profile_page()
        update_profile_page.enter_password("admin")
        update_profile_page.click_update_profile()

        # Kiểm tra xem thông báo thành công có xuất hiện hay không
        assert update_profile_page.is_password_length_error_message(), "Error message did not appear"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

