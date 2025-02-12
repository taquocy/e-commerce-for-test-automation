import unittest
import configparser
import HtmlTestRunner
import syss
import os

# Thêm đường dẫn đến thư mục gốc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import các class cần thiết
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):
    """Kiểm thử tính năng đăng nhập."""

    def setUp(self):
        """Thiết lập trình duyệt và điều hướng đến trang login."""
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.login_url = config['app']['login_url']

        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)

    def test_valid_login(self):
        """Đăng nhập với tài khoản hợp lệ."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("xuanhieu@gmail.com")
        login_page.enter_password("hieu1234")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        self.assertTrue(admin_page.check_admin_page_display(), "Không vào được trang Admin.")

    def test_invalid_login_wrong_password(self):
        """Đăng nhập thất bại do sai mật khẩu."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("xuanhieu@gmail.com")
        login_page.enter_password("wrongpassword")
        login_page.click_login()

        self.assertTrue(login_page.is_error_message_displayed(), "Không hiển thị lỗi khi nhập sai mật khẩu.")

    def test_invalid_login_non_existent_account(self):
        """Đăng nhập thất bại do tài khoản không tồn tại."""
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("nonexistent@gmail.com")
        login_page.enter_password("randompassword")
        login_page.click_login()

        self.assertTrue(login_page.is_error_message_displayed(), "Không hiển thị lỗi khi tài khoản không tồn tại.")

    def tearDown(self):
        """Đóng trình duyệt sau khi kiểm thử."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
