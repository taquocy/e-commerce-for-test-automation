import unittest
import configparser
import HtmlTestRunner
import sys
import os

from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage

# Thêm đường dẫn đến thư mục gốc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class HomePageTest(unittest.TestCase):
    """Kiểm thử trang chủ."""

    def setUp(self):
        """Thiết lập trình duyệt và điều hướng đến trang chủ."""
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.home_url = config['app']['home_url']

        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.home_url)

    def test_product_details_display(self):
        """Kiểm tra hiển thị thông tin sản phẩm."""
        home_page = HomePage(self.driver)

        self.assertTrue(home_page.get_product_title(), "Không hiển thị tiêu đề sản phẩm.")
        self.assertTrue(home_page.get_product_time(), "Không hiển thị thời gian sản phẩm.")
        self.assertTrue(home_page.get_product_price(), "Không hiển thị giá sản phẩm.")

    def test_add_to_basket(self):
        """Kiểm tra chức năng thêm vào giỏ hàng."""
        home_page = HomePage(self.driver)
        home_page.click_add_to_basket()
        self.assertTrue(home_page.is_item_added_to_basket(), "Sản phẩm không được thêm vào giỏ hàng.")

    def test_add_to_cart(self):
        """Kiểm tra chức năng thêm vào giỏ hàng (cart)."""
        home_page = HomePage(self.driver)
        home_page.click_add_to_cart()
        self.assertTrue(home_page.is_item_added_to_cart(), "Sản phẩm không được thêm vào giỏ hàng (cart).")

    def test_navigation_buttons(self):
        """Kiểm tra các nút điều hướng."""
        home_page = HomePage(self.driver)
        home_page.click_login()
        self.assertTrue(home_page.is_login_page_displayed(), "Không chuyển hướng đến trang đăng nhập.")
        
        self.driver.get(self.home_url)  # Quay lại trang chủ
        home_page.click_register()
        self.assertTrue(home_page.is_register_page_displayed(), "Không chuyển hướng đến trang đăng ký.")

    def test_search_functionality(self):
        """Kiểm tra chức năng tìm kiếm sản phẩm."""
        home_page = HomePage(self.driver)
        search_keyword = "Laptop"
        home_page.search_product(search_keyword)
        self.assertTrue(home_page.is_search_results_displayed(), "Kết quả tìm kiếm không hiển thị.")

    def test_filter_products(self):
        """Kiểm tra bộ lọc sản phẩm."""
        home_page = HomePage(self.driver)
        home_page.apply_filter("Price: Low to High")
        self.assertTrue(home_page.is_filter_applied(), "Bộ lọc sản phẩm không hoạt động.")

    def tearDown(self):
        """Đóng trình duyệt sau khi kiểm thử."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))