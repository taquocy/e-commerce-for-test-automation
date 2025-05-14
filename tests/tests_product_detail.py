import unittest
import configparser
import HtmlTestRunner
import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.product_detail_page import ProductDetailPage

class ProductDetailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Read config.ini
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')
        cls.product_url = cls.config['app'].get('product_url', '')

        # Initialize browser
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(cls.product_url)

        # Initialize ProductDetailPage
        cls.product_page = ProductDetailPage(cls.driver)

    def check_element_displayed(self, element_locator, description):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator))
        self.assertTrue(element.is_displayed(), f"❌ {description} không hiển thị!")

    def test_product_image_exists(self):
        self.check_element_displayed(self.product_page.product_image, "Hình ảnh sản phẩm")

    def test_product_name_not_empty(self):
        element = self.driver.find_element(*self.product_page.product_name)
        self.assertTrue(element.text.strip(), "❌ Tên sản phẩm trống!")

    def test_product_description_not_empty(self):
        element = self.driver.find_element(*self.product_page.product_description)
        self.assertTrue(element.text.strip(), "❌ Mô tả sản phẩm trống!")

    def test_product_price_not_empty(self):
        element = self.driver.find_element(*self.product_page.product_price)
        self.assertTrue(element.text.strip(), "❌ Giá sản phẩm trống!")

    def test_add_to_bag_button_exists(self):
        self.check_element_displayed(self.product_page.add_to_bag_button, "Nút Thêm vào giỏ hàng")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name='ProductDetailTestReport', report_title='Product Detail Test Report'))
