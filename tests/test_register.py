import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup


class RegisterTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.home_url = config['app']['home_url']       
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.home_url) 

    def test_valid_registration(self):
        register_page = RegisterPage(self.driver) 
        register_page.open_registration_form()
        register_page.enter_email("newuser2@gmail.com")
        register_page.enter_password("newpassword123")
        register_page.enter_confirm_password("newpassword123")
        register_page.click_register()

       
       
        input("Press Enter to close the browser...")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
