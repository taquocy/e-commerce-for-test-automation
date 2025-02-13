import unittest
import configparser

import HtmlTestRunner
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.product_detail import ProductDetail
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup

class ProductDetailTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.product_detail_url = config['app']['product_detail_url']

        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.product_detail_url)

    def test_product_detail_page(self):
        product_detail_page = ProductDetail(self.driver)
        product_detail_page.open_product_detail_page()
        product_detail_page.load_product_info("https://www.didongmy.com/vnt_upload/product/10_2020/thumbs/(600x600)_iphone_12_pro_max_gray_3.jpg","product_name_iphone",44-20000,"Hello Iphone")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
