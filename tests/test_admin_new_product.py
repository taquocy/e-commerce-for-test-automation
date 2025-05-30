import unittest
import configparser
import sys
import os
import logging
from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
import HtmlTestRunner
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CreateNewProductTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = cls.load_config()
        cls.driver = BrowserSetup.get_driver()
        cls.login_page = LoginPage(cls.driver)
        logging.info("Initialized browser and LoginPage")
        # Đăng nhập
        cls.driver.get(cls.config['app']['login_url'])
        cls.login_page.login(
            cls.config['app']['username'],
            cls.config['app']['password']
        )
        logging.info("Logged in successfully")
        time.sleep(2)

    @staticmethod
    def load_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def setUp(self):
        self.admin_page = AdminPage(self.driver)
        logging.info("Initialized AdminPage object")
        self.driver.get(self.config['app']['home_url'])
        time.sleep(1)

    def test_create_new_product(self):
        logging.info("Testing create new product")
        create_new_product_page = self.admin_page.open_new_product_page()
        self.assertTrue(self.admin_page.check_new_product_page_display(), "❌ New product page not displayed")
        
        create_new_product_page.enter_title("IPhone X")
        create_new_product_page.enter_description("This is Iphone 16 made in China")
        create_new_product_page.enter_price("3000")
        create_new_product_page.click_add_photo()
        create_new_product_page.enter_image_url("https://images.unsplash.com/photo-1726839662758-e3b5da59b0fb?q=80&w=2333&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        create_new_product_page.click_add_product()
        
        self.assertTrue(create_new_product_page.is_success_message_appeared(), "❌ Success message did not appear")

    @classmethod
    def tearDownClass(cls):
        logging.info("Closing browser")
        time.sleep(3)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='AdminNewProductTestReport',
        report_title='Admin New Product Test Report'
    ))