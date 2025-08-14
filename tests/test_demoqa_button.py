import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.demoqa_button import ButtonPage
from selenium.webdriver.support import expected_conditions as EC

class TestButtonPage(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.demoqa_url = ('https://demoqa.com/buttons')

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.demoqa_url)  # Sử dụng URL từ file config
        self.button_page = ButtonPage(self.driver)
    
    def test_button_clicks(self):
        self.button_page.double_click()
        self.button_page.right_click()
        self.button_page.dynamic_click()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
