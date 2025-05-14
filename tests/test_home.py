import unittest
import configparser
import sys
import os
from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
import HtmlTestRunner

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize the browser before running test cases"""
        cls.config = cls.load_config()
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(cls.config['app']['login_url'])

    @staticmethod
    def load_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def setUp(self):
        """Initialize the home page before each test case"""
        self.home_page = HomePage(self.driver)

    def test_product_details_display(self):
        self.assertTrue(self.home_page.get_product_title(), "❌ Product title is not displayed")
        self.assertTrue(self.home_page.get_product_time(), "❌ Product time is not displayed")
        self.assertTrue(self.home_page.get_product_price(), "❌ Product price is not displayed")

    def test_add_to_basket(self):
        self.home_page.click_add_to_basket()
        self.assertGreater(int(self.home_page.get_basket_count()), 0, "❌ Basket count did not increase")

    def test_add_to_cart(self):
        self.home_page.click_add_to_cart()
        self.assertGreater(int(self.home_page.get_cart_count()), 0, "❌ Cart count did not increase")

    def test_navigation_buttons(self):
        self.home_page.click_login()
        self.assertIn("signin", self.driver.current_url, "❌ Login page not opened")

        self.driver.back()

        self.home_page.click_register()
        self.assertIn("register", self.driver.current_url, "❌ Register page not opened")

    @classmethod
    def tearDownClass(cls):
        """Close the browser after all test cases"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name='HomePageTestReport', report_title='Home Page Test Report'))
