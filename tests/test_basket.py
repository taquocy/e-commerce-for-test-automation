import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from utils.browser_setup import BrowserSetup

class BasketTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang sản phẩm từ file config
        self.product_url = config['app']['product_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.product_url)  # Sử dụng URL từ file config

    def test_add_and_remove_from_basket(self):
        product_page = ProductPage(self.driver)
        basket_page = BasketPage(self.driver)

        # Thêm sản phẩm vào giỏ hàng
        product_page.add_to_basket()
        
        # Kiểm tra sản phẩm đã có trong giỏ hàng
        self.driver.get(config['app']['basket_url'])  # Điều hướng đến trang giỏ hàng
        product_name = basket_page.get_product_name()
        product_price = basket_page.get_product_price()

        # Xác nhận tên và giá của sản phẩm trong giỏ hàng đúng
        self.assertEqual(product_name, "IPhone 16 Pro Max 123")
        self.assertEqual(product_price, "3000$")


        # Xóa sản phẩm khỏi giỏ hàng
        basket_page.click_remove_from_basket()

        # Xác nhận sản phẩm đã bị xóa khỏi giỏ hàng
        self.assertTrue(basket_page.is_basket_empty(), "Giỏ hàng không trống như mong đợi sau khi xóa sản phẩm.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
