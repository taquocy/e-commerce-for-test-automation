# -*- coding: utf-8 -*-
import time
import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup
import time

class TextBox(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get("https://demoqa.com/text-box")  # Sử dụng URL từ file config

    def test_add_row_data_sucessesfully(self):

        #Step 1 Full Name box
        FullName = self.driver.find_element(By.XPATH,"//*[@id='userName']")
        FullName.send_keys("Nguyễn Văn A")
        #Step 2 the Email
        email = self.driver.find_element(By.XPATH,'//*[@id="userEmail"]')
        email.send_keys("nguyenvana@gmail.com")
        #Step 3 Current Address
        currentaddress = self.driver.find_element(By.XPATH,'//*[@id="currentAddress"]')
        currentaddress.send_keys("40 pham hung, BMT")
        #Step 4 User Permanent Address
        permanentaddress = self.driver.find_element(By.XPATH,'//*[@id="permanentAddress"]')
        permanentaddress.send_keys("daklak, vietnam")
        #Step 5 CLick on the Submit button
        submitBtn = self.driver.find_element(By.XPATH,'//*[@id="submit"]')
        submitBtn.click()
        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))