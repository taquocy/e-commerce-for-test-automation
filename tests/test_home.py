import unittest
import configparser
import sys
import os
import logging
from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
from pages.login_page import LoginPage
import HtmlTestRunner
import time

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Khởi tạo trình duyệt và đăng nhập một lần."""
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
        time.sleep(2)  # Đợi đăng nhập hoàn tất
        cls.driver.get(cls.config['app']['home_url'])
        logging.info(f"Navigated to {cls.config['app']['home_url']}")

    @staticmethod
    def load_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def setUp(self):
        """Khởi tạo trang Home trước mỗi test."""
        self.home_page = HomePage(self.driver)
        logging.info("Initialized HomePage object")
        # Điều hướng về trang chủ
        self.driver.get(self.config['app']['home_url'])
        time.sleep(1)  # Đợi trang tải

    def test_product_details_display(self):
        """Kiểm tra hiển thị thông tin sản phẩm."""
        logging.info("Testing product details display")
        self.assertTrue(self.home_page.get_product_title(), "❌ Product title is not displayed")
        self.assertTrue(self.home_page.get_product_time(), "❌ Product time is not displayed")
        self.assertTrue(self.home_page.get_product_price(), "❌ Product price is not displayed")

    def test_add_to_basket(self):
        """Kiểm tra chức năng thêm vào giỏ hàng."""
        logging.info("Testing add to basket")
        initial_count = self.home_page.get_basket_count()
        logging.info(f"Initial basket count: {initial_count}")
        self.home_page.click_add_to_basket()
        time.sleep(1)  # Đợi UI cập nhật
        new_count = self.home_page.get_basket_count()
        logging.info(f"New basket count: {new_count}")
        self.assertGreater(new_count, initial_count, "❌ Basket count did not increase after clicking Add to Basket")

    def test_navigation_buttons(self):
        """Kiểm tra nút điều hướng đến trang Profile."""
        logging.info("Testing navigation buttons")
        self.home_page.click_profile()
        time.sleep(1)  # Đợi trang tải
        self.assertIn("profile", self.driver.current_url, "❌ Profile page not opened")

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt."""
        logging.info("Closing browser")
        time.sleep(3)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name='HomePageTestReport', report_title='Home Page Test Report'))