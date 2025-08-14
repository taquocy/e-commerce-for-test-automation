import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.demoqa_webtables import webtables
from selenium.webdriver.support import expected_conditions as EC


class demoqa_webtables_test(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.demoqa_url = ('https://demoqa.com/webtables')

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.demoqa_url)  # Sử dụng URL từ file config

    def test_input(self):
        webtables_obj = webtables(self.driver)
        webtables_obj.click_delete1()
        webtables_obj.click_delete2()
        webtables_obj.click_delete3()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

