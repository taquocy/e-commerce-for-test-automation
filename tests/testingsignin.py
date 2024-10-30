# Luong Quang Hung testing python sign in GitHub: kudo-2003
import unittest
import configparser
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

        # Mở biểu mẫu đăng nhập
        login_page.open_login_form()

        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Kiểm tra xem trang quản trị có hiển thị hay không
        admin_page = AdminPage(self.driver)
        result = admin_page.check_admin_page_display()

        # Ghi kết quả vào file
        with open("LUONG_QUANG_HUNG.txt", "a") as f:
            if result:
                f.write("Login successful: Admin page displayed.\n")
            else:
                f.write("Login failed: Admin page not displayed.\n")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
