import unittest
import configparser
import HtmlTestRunner
import sys
import os
import random
import string

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.registration_page import RegistrationPage
from utils.browser_setup import BrowserSetup


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang đăng ký từ file config
        self.registration_url = config['app']['registration_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.registration_url)  # Sử dụng URL từ file config

    def generate_random_email(self):
        """Tạo email ngẫu nhiên với định dạng cơ bản."""
        letters = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{letters}@example.com"

    def test_valid_registration(self):
        registration_page = RegistrationPage(self.driver)

        registration_page.click_sign_up()
        # Nhập thông tin đăng ký hợp lệ
        random_email = self.generate_random_email()  # Tạo email ngẫu nhiên
        registration_page.enter_email(random_email)
        registration_page.enter_password("Password123")
        registration_page.enter_passwordConfirm("Password123")
        registration_page.click_register()

        # Kiểm tra thông báo thành công
        self.assertTrue(registration_page.is_registration_successful(), "Đăng ký thành công")


    def test_registration_with_existing_email(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.click_sign_up()

        # Nhập thông tin đăng ký với email đã tồn tại
        registration_page.enter_email("nguyen@gmail.com")  # Thay đổi thành email đã tồn tại trong CSDL
        registration_page.enter_password("123456")
        registration_page.enter_passwordConfirm("123456")
        registration_page.click_register()

        # Kiểm tra thông báo lỗi
        error_message = registration_page.get_error_message()
        # email_error_message = registration_page.get_email_in_use_error_message()
        # self.assertEqual(email_error_message, "This e-mail already using.")
        self.assertEqual(error_message, "This e-mail already using.")  # Thay đổi thông báo lỗi nếu cần

    def test_registration_with_mismatched_passwords(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.click_sign_up()

        # Nhập thông tin đăng ký với mật khẩu không khớp
        random_email = self.generate_random_email()  # Tạo email ngẫu nhiên
        registration_page.enter_email(random_email)
        registration_page.enter_password("Password123")
        registration_page.enter_passwordConfirm("DifferentPassword123")
        registration_page.click_register()

        # Kiểm tra thông báo lỗi
        error_message = registration_page.get_error_message()
        self.assertEqual(error_message, "Mật khẩu xác nhận không khớp!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
