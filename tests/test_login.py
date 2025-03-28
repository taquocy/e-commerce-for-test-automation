import unittest
import configparser
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.login_url = config['app']['login_url']
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)

    def test_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Đã đổi username từ superadmin@gmail.com thành tuankiet
        login_page.enter_username("tuankiet")  # <-- Đây là dòng đã sửa
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))