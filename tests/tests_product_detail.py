import unittest
import configparser
import HtmlTestRunner
import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.product_detail_page import ProductDetailPage


class ProductDetailTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Khởi tạo trình duyệt và tải trang sản phẩm một lần trước khi chạy test """
        config = configparser.ConfigParser()
        config.read('config.ini')
        cls.product_url = config['app'].get('product_url', '')

        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(cls.product_url)
        cls.product_page = ProductDetailPage(cls.driver)
        cls.wait = WebDriverWait(cls.driver, 10)  # Chờ tối đa 10 giây để tìm thấy phần tử

    def setUp(self):
        """ Load lại trang để đảm bảo trạng thái ban đầu cho mỗi test """
        self.driver.refresh()

    def find_element(self, locator):
        """ Hàm tìm phần tử với WebDriverWait để đảm bảo phần tử đã tải """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.fail(f"❌ Không tìm thấy phần tử {locator}")

    def test_product_image_exists(self):
        """ Kiểm tra hình ảnh sản phẩm có tồn tại """
        element = self.find_element(self.product_page.product_image)
        self.assertTrue(element.is_displayed(), "❌ Hình ảnh sản phẩm không hiển thị!")
        print("✅ Hình ảnh sản phẩm hiển thị đúng!")

    def test_product_name_not_empty(self):
        """ Kiểm tra tên sản phẩm không rỗng """
        element = self.find_element(self.product_page.product_name)
        text = element.text.strip()
        self.assertTrue(text, "❌ Tên sản phẩm trống!")
        print(f"✅ Tên sản phẩm: {text}")

    def test_product_description_not_empty(self):
        """ Kiểm tra mô tả sản phẩm không rỗng """
        element = self.find_element(self.product_page.product_description)
        text = element.text.strip()
        self.assertTrue(text, "❌ Mô tả sản phẩm trống!")
        print(f"✅ Mô tả sản phẩm: {text}")

    def test_product_price_not_empty(self):
        """ Kiểm tra giá sản phẩm không rỗng """
        element = self.find_element(self.product_page.product_price)
        text = element.text.strip()
        self.assertTrue(text, "❌ Giá sản phẩm trống!")
        print(f"✅ Giá sản phẩm: {text}")

    def test_add_to_bag_button_exists(self):
        """ Kiểm tra nút Thêm vào giỏ hàng có tồn tại """
        element = self.find_element(self.product_page.add_to_bag_button)
        self.assertTrue(element.is_displayed(), "❌ Nút Thêm vào giỏ hàng không hiển thị!")
        print("✅ Nút Thêm vào giỏ hàng hiển thị đúng!")

    @classmethod
    def tearDownClass(cls):
        """ Đóng trình duyệt sau khi tất cả test hoàn thành """
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
