import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.product_detail import ProductDetail
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class ProductDetailTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang Product detail từ file config
        self.product_detail_url = config['app']['product_detail_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.product_detail_url)  # Sử dụng URL từ file config

    def test_product_detail_page(self):
        product_detail_page = ProductDetail(self.driver)
        product_detail_page.open_product_detail_page()
        product_detail_page.load_product_info("https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m302qqcpre282b.webp","product_name_iphone",300,"áo khoác nam mùa đông")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))