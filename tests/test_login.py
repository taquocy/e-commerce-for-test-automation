import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Read config.ini
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')

        # Initialize browser
        cls.driver = BrowserSetup.get_driver()

    def setUp(self):
        # Get login URL from config
        self.login_url = self.config['app']['login_url']
        self.driver.get(self.login_url)

    def test_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)
        login_page.login("superadmin@gmail.com", "admin123")

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name='LoginTestReport', report_title='Login Test Report'))
