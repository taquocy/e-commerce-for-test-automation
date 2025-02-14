import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.product_detail_page import ProductDetailtPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang chi tiết sản phẩm từ file config
        self.product_url = config['app']['product_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.product_url)  # Điều hướng đến trang sản phẩm

        # Khởi tạo trang sản phẩm
        self.product_page = ProductDetailtPage(self.driver)

    def test_product_image_exists(self):
        """ Kiểm tra hình ảnh sản phẩm có tồn tại """
        element = self.driver.find_element(*self.product_page.product_image)
        self.assertTrue(element.is_displayed(), "❌ Hình ảnh sản phẩm không hiển thị!")
        print("✅ Hình ảnh sản phẩm hiển thị đúng!")

    def test_product_name_not_empty(self):
        """ Kiểm tra tên sản phẩm không rỗng """
        element = self.driver.find_element(*self.product_page.product_name)
        text = element.text.strip()
        self.assertTrue(text, "❌ Tên sản phẩm trống!")
        print(f"✅ Tên sản phẩm: {text}")

    def test_product_description_not_empty(self):
        """ Kiểm tra mô tả sản phẩm không rỗng """
        element = self.driver.find_element(*self.product_page.product_description)
        text = element.text.strip()
        self.assertTrue(text, "❌ Mô tả sản phẩm trống!")
        print(f"✅ Mô tả sản phẩm: {text}")

    def test_product_price_not_empty(self):
        """ Kiểm tra giá sản phẩm không rỗng """
        element = self.driver.find_element(*self.product_page.product_price)
        text = element.text.strip()
        self.assertTrue(text, "❌ Giá sản phẩm trống!")
        print(f"✅ Giá sản phẩm: {text}")

    def test_add_to_bag_button_exists(self):
        """ Kiểm tra nút Thêm vào giỏ hàng có tồn tại """
        element = self.driver.find_element(*self.product_page.add_to_bag_button)
        self.assertTrue(element.is_displayed(), "❌ Nút Thêm vào giỏ hàng không hiển thị!")
        print("✅ Nút Thêm vào giỏ hàng hiển thị đúng!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))