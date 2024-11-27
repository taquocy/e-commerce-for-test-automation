import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url) 
        
    # Code here
    def test_valid_register(self):
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()
        # type input
        register_page.enter_email("truonghai9426@gmail.com")
        register_page.enter_password("truonghai123")
        register_page.enter_passwordConfirm("truonghai123")

        register_page.click_register()

        # assert register_page.is_success_message_appeared()

    def test_email_or_confirm_password_invalid(self):
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()

        register_page.enter_email("truonghai9426@gmail.com")
        register_page.enter_password("truonghai123")
        register_page.enter_passwordConfirm("truonghai12")

        register_page.click_register()

        # Verify email or password confirm invalid
        error_message = register_page.get_error_message()
        self.assertEqual(error_message, "The email or password confirm must be valid")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

