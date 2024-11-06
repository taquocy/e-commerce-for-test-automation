import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditProductPage(unittest.TestCase):

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

    def test_edit_product_successfully(self):
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page= admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("")
        create_edit_product_page.enter_title("product is testting MinhHauDev")
        create_edit_product_page.enter_description("")
        create_edit_product_page.enter_description("it is performed by Minh Hau Dev")
        create_edit_product_page.enter_price("")
        create_edit_product_page.enter_price("3000")
        # create_edit_product_page.click_add_photo()
        create_edit_product_page.enter_image_url("https://images/for-me")
        create_edit_product_page.click_add_product()
        # Kiểm tra xem thông báo thành công có xuất hiện hay không
        # assert create_new_product_page.is_success_message_appeared(), "Success message did not appear"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

