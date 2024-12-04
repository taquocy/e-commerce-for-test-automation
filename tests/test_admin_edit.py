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


class EditProductPage(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)
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
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("nnnn")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_edit_product_fail(self):
        # nhung gia tri khong hop le
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("")
        create_edit_product_page.enter_description("qq")
        create_edit_product_page.enter_price("0")
        create_edit_product_page.enter_image_url("")
        create_edit_product_page.click_add_product()

    def test_blank_title(self):
        # để trống tiêu đề
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("")
        create_edit_product_page.enter_description("mo ta abc")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_blank_description(self):
        # để trống mô tả
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_description_invalid(self):
        # tối thiểu 5 kí tự
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("12")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_blank_price(self):
        # để trống giá
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("mo ta abc")
        create_edit_product_page.enter_price("")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_invalid_price(self):
        # nhập giá không hợp lệ là kí tự chữ, kí tự đặc biệt
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("mo ta abc")
        create_edit_product_page.enter_price("abcd#@!")
        create_edit_product_page.enter_image_url(
            "https://www.google.com/imgres?q=%E1%BA%A3nh%20meof&imgurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Fwp-content%2Fuploads%2F2024%2F02%2Favatar-anh-meo-cute-1.jpg&imgrefurl=https%3A%2F%2Fcellphones.com.vn%2Fsforum%2Favatar-anh-meo-cute&docid=knQo0pbvtkObCM&tbnid=t40Etp5a7j_CXM&vet=12ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA..i&w=800&h=800&hcb=2&ved=2ahUKEwjBod7k5PyJAxVvkVYBHWSqNN8QM3oECB4QAA")
        create_edit_product_page.click_add_product()

    def test_blank_photos(self):
        # để trống ảnh
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("mo ta abc")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url("")
        create_edit_product_page.click_add_product()

    def test_invalid_photos(self):
        # để trống ảnh
        admin_page = AdminPage(self.driver)
        admin_page.open_admin_page()
        admin_page.open_edit_or_delete_product_page()
        create_edit_product_page = admin_page.open_edit_product_page()
        create_edit_product_page.enter_title("IPHONE")
        create_edit_product_page.enter_description("mo ta abc")
        create_edit_product_page.enter_price("3000")
        create_edit_product_page.enter_image_url("12@#@!!!")
        create_edit_product_page.click_add_product()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

