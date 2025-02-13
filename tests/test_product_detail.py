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
        product_detail_page.load_product_info("https://cdnv2.tgdd.vn/mwg-static/tgdd/Products/Images/42/329149/iphone-16-pro-max-titan-tu-nhien-2-638638962819617092-750x500.jpg","product_name_iphone",44-20000,"hello Iphone")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

