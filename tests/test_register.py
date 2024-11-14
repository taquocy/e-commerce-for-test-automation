import unittest
import configparser
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup
import HtmlTestRunner

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang register từ file config
        self.register_url = config['app']['login_url']  

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.register_url)  # Sử dụng URL từ file config

    def test_valid_register(self):
        # Trường hợp đăng ký hợp lệ
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()
        register_page.enter_email("testuser2@gmail.com")
        register_page.enter_password("password123")
        register_page.enter_confirm_password("password123")
        register_page.click_register_button()

        # Kiểm tra đăng ký thành công
        try:
            register_page.check_registration_success()
            print("Đăng ký thành công.")
        except Exception as e:
            self.fail(f"Đăng ký hợp lệ thất bại: {e}")

    def test_invalid_register_password_mismatch(self):
        # Trường hợp mật khẩu xác nhận không khớp
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()
        register_page.enter_email("testuser2@gmail.com")
        register_page.enter_password("password123")
        register_page.enter_confirm_password("password321")  # Mật khẩu không khớp
        register_page.click_register_button()

        # Kiểm tra thông báo lỗi xác nhận mật khẩu không khớp
        try:
            error_message = self.driver.find_element(By.ID, "passwordMismatchError")
            self.assertTrue(error_message.is_displayed(), "Thông báo lỗi không xuất hiện khi mật khẩu không khớp.")
        except Exception as e:
            self.fail(f"Không tìm thấy thông báo lỗi khi mật khẩu không khớp: {e}")

    def test_invalid_register_empty_fields(self):
        # Trường hợp không điền thông tin đăng ký
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()
        register_page.enter_email("")  # Không nhập email
        register_page.enter_password("")  # Không nhập mật khẩu
        register_page.enter_confirm_password("")  # Không nhập mật khẩu xác nhận
        register_page.click_register_button()

        # Kiểm tra lỗi các trường bắt buộc
        try:
            error_message = self.driver.find_element(By.ID, "emptyFieldsError")
            self.assertTrue(error_message.is_displayed(), "Thông báo lỗi không xuất hiện khi bỏ trống các trường.")
            print("Hãy nhập thông tin đăng ký")
        except Exception as e:
            self.fail(f"Không tìm thấy thông báo lỗi khi các trường trống: {e}")

    def tearDown(self):
        # Đóng trình duyệt sau mỗi lần kiểm thử
        self.driver.quit()

if __name__ == "__main__":
    # Chạy tất cả các test và tạo báo cáo HTML
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
