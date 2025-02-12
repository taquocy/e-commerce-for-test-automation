import unittest
import configparser
import sys
import os
from utils.browser_setup import BrowserSetup
from pages.home_page import HomePage
import HtmlTestRunner

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class HomePageTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Khởi tạo trình duyệt trước khi chạy các test case"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        cls.home_url = config['app']['login_url']
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(cls.home_url)

    def test_product_details_display(self):
        """Kiểm tra thông tin chi tiết của sản phẩm"""
        home_page = HomePage(self.driver)

        product_title = home_page.get_product_title()
        product_time = home_page.get_product_time()
        product_price = home_page.get_product_price()

        self.assertTrue(product_title, "Product title is not displayed")
        self.assertTrue(product_time, "Product time is not displayed")
        self.assertTrue(product_price, "Product price is not displayed")

    def test_add_to_basket(self):
        """Kiểm tra thêm sản phẩm vào giỏ hàng"""
        home_page = HomePage(self.driver)
        home_page.click_add_to_basket()
        
        # Kiểm tra sản phẩm đã được thêm thành công (ví dụ kiểm tra thông báo hoặc số lượng)
        basket_count = home_page.get_basket_count()
        self.assertGreater(int(basket_count), 0, "Basket count did not increase")

    def test_add_to_cart(self):
        """Kiểm tra thêm sản phẩm vào cart"""
        home_page = HomePage(self.driver)
        home_page.click_add_to_cart()

        # Kiểm tra giỏ hàng có sản phẩm hay không
        cart_count = home_page.get_cart_count()
        self.assertGreater(int(cart_count), 0, "Cart count did not increase")

    def test_navigation_buttons(self):
        """Kiểm tra điều hướng trang đăng nhập và đăng ký"""
        home_page = HomePage(self.driver)

        home_page.click_login()
        self.assertIn("signin", self.driver.current_url, "Login page not opened")

        self.driver.back()

        home_page.click_register()
        self.assertIn("register", self.driver.current_url, "Register page not opened")

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt sau khi chạy tất cả test case"""
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
