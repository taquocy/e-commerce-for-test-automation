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
        self.driver.get("https://demoqa.com/webtables")  # Sử dụng URL từ file config

    def test_add_row_data_sucessesfully(self):

        #Step 1 Click on Add button
        addBtn = self.driver.find_element(By.XPATH,"//button[@id='addNewRecordButton']")
        addBtn.click()
        #Step 2 Fill in the First Name
        firstName = self.driver.find_element(By.XPATH,"//input[@id='firstName']")
        firstName.send_keys("IT23M")
        #Step 3 Last Name,
        lastName = self.driver.find_element(By.XPATH,"//input[@id='lastName']")
        lastName.send_keys("UDA University")
        #Step 4 User Email,
        email = self.driver.find_element(By.XPATH,"//input[@id='userEmail']")
        email.send_keys("ytq@donga.edu.vn")
        #Step 5 Age,
        age = self.driver.find_element(By.XPATH,"//input[@id='age']")
        age.send_keys("40")
        #Step 6 Salary
        salary = self.driver.find_element(By.XPATH,"//input[@id='salary']")
        salary.send_keys("5000")
        #Step 7 Department
        department = self.driver.find_element(By.XPATH,"//input[@id='department']")
        department.send_keys("IT")
        #Step 8 Click on Submit button
        submitBtn = self.driver.find_element(By.XPATH,"//button[@id='submit']")
        submitBtn.click()
        #Step 9 Verify the data is added to the table
        table = self.driver.find_element(By.XPATH,"//div[@class='rt-table']")
        assert "IT23M" in table.text, "Thêm dữ liệu thất bại!"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

