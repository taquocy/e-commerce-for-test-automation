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
from pages.update_product import UpdateProduct  # Import lớp mới cho trang cập nhật
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpdateProductTest(unittest.TestCase):

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

    def test_update_product_successfully(self):
        # Điều hướng tới trang cập nhật sản phẩm
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        update_product_page = admin_page.open_update_product_page()

        # Cập nhật thông tin sản phẩm
        update_product_page.enter_title("IPhone 16 Pro Max - Updated")
        update_product_page.enter_description("This is the updated description for Iphone 16")
        update_product_page.enter_price("3500")
        update_product_page.click_add_photo()
        update_product_page.enter_image_url("https://images.unsplash.com/photo-1726839662758-e3b5da59b0fb?q=80&w=2333&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        update_product_page.click_update_product()  # Nút cập nhật sản phẩm

        # Kiểm tra xem thông báo cập nhật thành công có xuất hiện hay không
        success = update_product_page.is_success_message_appeared()
        self.assertTrue(success, "Success message did not appear after updating the product")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))