import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.Home_page import HomePage


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Thiết lập ban đầu, chỉ chạy một lần trước tất cả các bài kiểm tra."""
        # Đọc file config.ini để lấy cấu hình
        config = configparser.ConfigParser()
        config.read('config.ini')
        cls.home_url = config['app']['home_url']

    def setUp(self):
        """Thiết lập trước mỗi bài kiểm tra."""
        # Khởi tạo trình duyệt và trang chủ
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.home_url)
        self.home_page = HomePage(self.driver)

    def test_add_to_basket_button_displayed(self):
        """Kiểm tra xem nút 'Add to Basket' có hiển thị trên trang không."""
        self.assertTrue(
            self.home_page.is_add_to_basket_button_displayed(),
            "Nút 'Add to Basket' không hiển thị."
        )

    def test_add_to_cart_button_displayed(self):
        """Kiểm tra xem nút 'Add to Cart' có hiển thị trên trang không."""
        self.assertTrue(
            self.home_page.is_add_to_cart_button_displayed(),
            "Nút 'Add to Cart' không hiển thị."
        )

    def test_load_more_button_displayed(self):
        """Kiểm tra xem nút 'Load More' có hiển thị trên trang không."""
        self.assertTrue(
            self.home_page.is_load_more_button_displayed(),
            "Nút 'Load More' không hiển thị."
        )

    def test_load_more_functionality(self):
        """Kiểm tra chức năng của nút 'Load More'."""
        self.home_page.click_load_more()
        self.assertTrue(
            self.home_page.wait_for_load_more_results(),
            "Nội dung mới không được tải sau khi nhấn 'Load More'."
        )

    def tearDown(self):
        """Đóng trình duyệt sau mỗi bài kiểm tra."""
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        """Dọn dẹp tài nguyên chung sau khi tất cả bài kiểm tra hoàn thành."""
        print("Hoàn tất tất cả các bài kiểm tra.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
