import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang chủ từ file config
        self.home_url = config['app']['home_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.home_url)  # Sử dụng URL từ file config
        self.home_page = HomePage(self.driver)

    def test_add_to_basket_button_displayed(self):
        """Kiểm tra xem nút 'Add to Basket' có hiển thị trên trang không."""
        self.assertTrue(self.home_page.is_add_to_basket_button_displayed(), "Nút 'Add to Basket' không hiển thị.")

    def test_add_to_cart_button_displayed(self):
        """Kiểm tra xem nút 'Add to Cart' có hiển thị trên trang không."""
        self.assertTrue(self.home_page.is_add_to_cart_button_displayed(), "Nút 'Add to Cart' không hiển thị.")

    def test_load_more_button_displayed(self):
        """Kiểm tra xem nút 'Load More' có hiển thị trên trang không."""
        self.assertTrue(self.home_page.is_load_more_button_displayed(), "Nút 'Load More' không hiển thị.")

    def test_load_more_functionality(self):
        """Kiểm tra chức năng của nút 'Load More'."""
        self.assertTrue(self.home_page.test_load_more(), "Nội dung mới không được tải sau khi nhấn 'Load More'.")

    def test_add_and_remove_basket_button(self):
        """Kiểm tra chức năng của nút 'Add to Basket, Remove from Basket'."""
        self.assertTrue(self.home_page.test_toggle_basket_button(), "Nút 'add_basket' và 'remove_basket' không hoạt động")

    def test_navigate(self):
        self.assertTrue(self.home_page.test_navigate_to_item_detail(), "Không chuyển trang khi nhấn vào item")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))