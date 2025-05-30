import unittest
import configparser
import HtmlTestRunner
import sys
import os, time

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup
from testdata.login_data import login_test_cases

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Read config.ini
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')

        # Initialize browser
        cls.driver = BrowserSetup.get_driver()

    def setUp(self):
        # Khởi tạo browser mới cho mỗi testcase
        self.driver = BrowserSetup.get_driver()
        self.login_url = self.config['app']['login_url']
        self.driver.get(self.login_url)

    def tearDown(self):
        time.sleep(1)  # Chờ để browser đóng hoàn toàn
        self.driver.quit()

    def login_and_check(self, username, password, expect_success):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        time.sleep(1)
        if expect_success:
            self.assertIn("/profile", self.driver.current_url, "❌ Login should succeed but did not redirect to profile")
        else:
            self.assertIn("/signin", self.driver.current_url, "❌ Login should fail but did not stay on signin page")

    def test_login_cases(self):
        for case in login_test_cases:
            with self.subTest(msg=case["case"]):
                self.driver.get(self.login_url)
                self.login_and_check(case["username"], case["password"], case["expect_success"])


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='LoginTestReport',
        report_title='Login Test Report'
    ))