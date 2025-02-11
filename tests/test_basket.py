import unittest
import configparser
import HtmlTestRunner
import sys
import os
import time

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from utils.browser_setup import BrowserSetup


class BasketTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_add_to_basket_button_display(self):
        # Đăng nhập
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("0961147280q@gmail.com")
        login_page.enter_password("12345678")
        login_page.click_login()

        # Quay về trang chủ và thêm sản phẩm vào giỏ hàng
        basket_page = BasketPage(self.driver)
        basket_page.go_home()  # Quay về trang chủ
        time.sleep(1)
        basket_page.add_to_basket()  # Thêm sản phẩm vào giỏ hàng
        time.sleep(1)

        # Kiểm tra nút giỏ hàng có hiển thị sau khi thêm sản phẩm
        self.assertTrue(basket_page.is_basket_button_displayed(), "Nút giỏ hàng không hiển thị sau khi thêm sản phẩm.")

    def test_remove_from_basket_button_display(self):
        # Đăng nhập
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        login_page.enter_username("0961147280q@gmail.com")
        login_page.enter_password("12345678")
        login_page.click_login()

        # Quay về trang chủ và thêm sản phẩm vào giỏ hàng
        basket_page = BasketPage(self.driver)
        basket_page.go_home()  # Quay về trang chủ
        time.sleep(1)
        basket_page.add_to_basket()  # Thêm sản phẩm vào giỏ hàng
        time.sleep(1)

        # Mở giỏ hàng và xóa sản phẩm khỏi giỏ hàng
        basket_page.open_basket()  # Mở giỏ hàng
        time.sleep(1)
        basket_page.remove_item()  # Xóa sản phẩm khỏi giỏ hàng
        time.sleep(1)

        # Kiểm tra nút giỏ hàng không hiển thị sau khi xóa sản phẩm
        self.assertFalse(basket_page.is_basket_button_displayed(), "Nút giỏ hàng vẫn hiển thị sau khi xóa sản phẩm.")

    def tearDown(self):
        # Đóng trình duyệt
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
