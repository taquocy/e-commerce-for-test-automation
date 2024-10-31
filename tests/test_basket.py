import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from utils.browser_setup import BrowserSetup

class AddToBasketTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()
        
    def test_add_product_to_basket(self):
        
        home_page = HomePage(self.driver)

        # Thực hiện hành động "Add to Basket"
        home_page.open_home()
        home_page.click_add_to_basket()
        
        basket_page = BasketPage(self.driver)
        basket_page.open_basket()
        
        print('Total price:', basket_page.get_total_price())
        print('Item image:', basket_page.get_item_image_src())
        
        basket_page.remove_item_from_basket()
        print('Removed item successfully')
        home_page.open_home()
        

        # Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng thành công

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
