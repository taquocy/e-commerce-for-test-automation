import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.democa_text_box import text_box
from selenium.webdriver.support import expected_conditions as EC


class CreateNewProductTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.demoqa_url = ('https://demoqa.com/text-box')

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.demoqa_url)  # Sử dụng URL từ file config

    def test_input(self):
        # Tạo đối tượng của lớp text_box
        text_box_obj = text_box(self.driver)
        
        # Gọi các phương thức từ đối tượng text_box
        text_box_obj.enter_fullname("Họ và Tên")
        text_box_obj.enter_email("ex@mail.com")
        text_box_obj.enter_address("Địa chỉ")
        text_box_obj.enter_paddress("Địa chỉ")
        text_box_obj.click_submit()
        # Kiểm tra xem thông báo thành công có xuất hiện hay không
        # assert create_new_product_page.is_success_message_appeared(), "Success message did not appear"


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

