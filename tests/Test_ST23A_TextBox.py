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

class WebTablePage(unittest.TestCase):

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

        
        #Step 1 Fill in the First Name
        fulltName = self.driver.find_element(By.XPATH,"//input[@id='userName']")
        fulltName.send_keys("Lê Duy")
        #Step 2 User Email,
        email = self.driver.find_element(By.XPATH,"//input[@id='userEmail']")
        email.send_keys("duy188@gmail.com")

        #Step 3 CurrentAddress
        CurrentAddress = self.driver.find_element(By.XPATH,"//input[@id='currentAddress']")
        CurrentAddress.send_keys("80binhhoa15")
        #Step 4 Permanent Address
        PermanentAddress = self.driver.find_element(By.XPATH,"//input[@id='permanentAddress']")
        PermanentAddress.send_keys("80binhhoa15, Cẩm lệ")
        #Step 5 Click on Submit button
        submitBtn = self.driver.find_element(By.XPATH,"//button[@id='submit']")
        submitBtn.click()
        #Step 6 Verify the data is added to the table
        textbox = self.driver.find_element(By.XPATH,"//div[@class='rt-textbox']")
        assert "IT23M" in textbox.text, "Thêm dữ liệu thất bại!"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))