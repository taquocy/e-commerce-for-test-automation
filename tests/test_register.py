import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class RegisterTest(unittest.TestCase):

   def setUp(self):
      # Đọc file config.ini
      config = configparser.ConfigParser()
      config.read('config.ini')

      # Lấy URL trang login từ file config
      self.signup_url = config['app']['signup_url']

      # Khởi tạo trình duyệt
      self.driver = BrowserSetup.get_driver()
      self.driver.get(self.signup_url)  # Sử dụng URL từ file config

   def test_valid_register(self):
      signup_page = RegisterPage(self.driver)

      signup_page.open_register_form()
      # Nhập thông tin đăng nhập
      signup_page.enter_username("tuanpham@gmail.com")
      signup_page.enter_password("tuanpham")
      signup_page.enter_password_confirm("tuanpham")
      signup_page.click_register()


   def tearDown(self):
      self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

