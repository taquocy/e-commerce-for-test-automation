import unittest
import configparser
import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.demoqa_radio_button import RadioPage
from selenium.webdriver.support import expected_conditions as EC

class TestRadioPage(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.demoqa_url = ('https://demoqa.com/radio-button')

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.demoqa_url)
        self.radio_page = RadioPage(self.driver)
    
    def test_select_radio_buttons(self):
        self.radio_page.click_yes()
        self.assertEqual(self.radio_page.get_selected_text(), "Yes")
        
        self.radio_page.click_impressive()
        self.assertEqual(self.radio_page.get_selected_text(), "Impressive")
        
        self.assertTrue(self.radio_page.is_no_disabled())
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
